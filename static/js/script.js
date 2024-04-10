document.addEventListener('DOMContentLoaded', function() {
    var subDiv = document.getElementById('sub');
    var logo = document.getElementById('logo');
    var newsItems = document.querySelectorAll('.news-item'); 
    const searchQuery = document.getElementById('searchQuery');
    const suggestionsBox = document.getElementById('searchSuggestions');
    const filterChoice = document.getElementById('filterChoice');

    function setCursor(element) {
        element.addEventListener('mouseenter', function() {
            element.style.cursor = 'pointer';
        });

        element.addEventListener('mouseleave', function() {
            element.style.cursor = 'default';
        });
    }

    function setClickEvent(element, url) {
        element.addEventListener('click', function() {
            window.location.href = url;
        });
    }

    setCursor(logo);
    setClickEvent(logo, '/');

    setCursor(subDiv);
    setClickEvent(subDiv, 'https://www.whatsapp.com/channel/0029VaC8d1M3AzNVm4DlYk2H');

    searchQuery.addEventListener('input', function(e) {
        const query = e.target.value;
        if (query.length < 3) {
            suggestionsBox.innerHTML = '';
            return;
        }

        fetch('/search', {
            method: 'POST',
            body: JSON.stringify({query: query}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            suggestionsBox.innerHTML = '';
            data.forEach(item => {
                const suggestionItem = document.createElement('div');
                suggestionItem.style.display = 'flex';
                suggestionItem.style.alignItems = 'center';
                suggestionItem.style.cursor = 'pointer';

                const img = document.createElement('img');
                img.src = item.image;
                img.alt = 'News Image';
                img.style.width = '10rem';  
                img.style.height = '6rem';
                img.style.marginRight = '10px';

                const title = document.createElement('div');
                title.textContent = item.title;

                suggestionItem.appendChild(img);
                suggestionItem.appendChild(title);

                suggestionItem.addEventListener('click', () => {
                    window.location.href = item.url;
                });

                suggestionsBox.appendChild(suggestionItem);
            });
        })
        .catch(error => console.error('Error:', error));
    });

    document.body.addEventListener('click', () => {
        suggestionsBox.innerHTML = ''; 
    }, true);


    newsItems.forEach(function(item) {
        setCursor(item); 
        var route = item.getAttribute('data-route');
        setClickEvent(item, route);
    });


    function fetchAndUpdateNews() {
        const choice = filterChoice.value;
        
        fetch('/filter_news', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({filter_choice: choice}),
        })
        .then(response => response.json())
        .then(data => {
            updateNewsList(data);
        })
        .catch(error => console.error('Error:', error));
    }


    filterChoice.addEventListener('change', fetchAndUpdateNews);

    function updateNewsList(newsData) {
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = ''; 

        newsData.forEach(newsItem => {
            const newsElement = document.createElement('div');
            newsElement.style.cursor = 'pointer';
            newsElement.innerHTML = `
                <h2>${newsItem.title}</h2>
                <img src="${newsItem.image}" alt="News Image" style="width: 100px; height: 60px;">
                <p>Date: ${newsItem.date}</p>
            `;

            newsContainer.appendChild(newsElement);
            newsElement.setAttribute('data-route', newsItem.url);


            newsElement.addEventListener('click', function() {
                const route = this.getAttribute('data-route');
                window.location.href = route;
            });
    
            newsContainer.appendChild(newsElement);
    
        });
    }

    fetchAndUpdateNews();



    const totalPages = 3; 
    let currentPage = 1;

    function showPage(pageNumber) {

        const pages = document.querySelectorAll('.news-page');
        pages.forEach(page => {
            page.style.display = 'none';
        });
       
        const currentPageDiv = document.getElementById('page' + pageNumber);
        if (currentPageDiv){
            currentPageDiv.style.display ='flex'
        }
    }

    function setupPaginationControls() {
        const paginationControls = document.getElementById('paginationControls');
        paginationControls.innerHTML = '';

        const prevButton = document.createElement('button');
        prevButton.textContent = 'Previous';
        prevButton.disabled = currentPage === 1;
        prevButton.addEventListener('click', function() {
            if (currentPage > 1) {
                currentPage--;
                updatePagination();
            }
        });
        paginationControls.appendChild(prevButton);


        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i;
            pageButton.disabled = i === currentPage; 
            pageButton.addEventListener('click', function() {
                currentPage = i;
                updatePagination();
            });
            paginationControls.appendChild(pageButton);
        }


        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next';
        nextButton.disabled = currentPage === totalPages; 
        nextButton.addEventListener('click', function() {
            if (currentPage < totalPages) {
                currentPage++;
                updatePagination();
            }
        });
        paginationControls.appendChild(nextButton);
    }

    function updatePagination() {
        showPage(currentPage);
        setupPaginationControls();
    }

    
    updatePagination();

});
