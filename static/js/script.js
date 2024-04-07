document.addEventListener('DOMContentLoaded', function() {
    var subDiv = document.getElementById('sub');
    var logo = document.getElementById('logo');
    var newsItems = document.querySelectorAll('.news-item'); // Select all news items
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
                img.style.width = '10rem';  // Set the image size
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
        suggestionsBox.innerHTML = ''; // Clear suggestions when clicking outside
    }, true);




    // New: Iterate over each news item to add cursor style and click event
    newsItems.forEach(function(item) {
        setCursor(item); // Apply cursor style on hover
        // Use the data-route attribute for the URL in the click event
        var route = item.getAttribute('data-route');
        setClickEvent(item, route);
    });

    // Function to fetch and update news list based on the selected filter
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

    // Update news list when the filter choice changes
    filterChoice.addEventListener('change', fetchAndUpdateNews);

    function updateNewsList(newsData) {
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = ''; // Clear current news

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

            // Add click event listener to redirect based on data-route
            newsElement.addEventListener('click', function() {
                const route = this.getAttribute('data-route');
                window.location.href = route;
            });
    
            newsContainer.appendChild(newsElement);
    
        });
    }

    // Automatically fetch and display the latest news on page load
    fetchAndUpdateNews();



    const totalPages = 3; // Total number of pages
    let currentPage = 1;

    function showPage(pageNumber) {
        // Hide all pages
        const pages = document.querySelectorAll('.news-page');
        pages.forEach(page => {
            page.style.display = 'none';
        });
        // Show the current page
        const currentPageDiv = document.getElementById('page' + pageNumber);
        if (currentPageDiv){
            currentPageDiv.style.display ='flex'
        }
    }

    function setupPaginationControls() {
        const paginationControls = document.getElementById('paginationControls');
        paginationControls.innerHTML = ''; // Clear existing controls

        // Previous button
        const prevButton = document.createElement('button');
        prevButton.textContent = 'Previous';
        prevButton.disabled = currentPage === 1; // Disable if on the first page
        prevButton.addEventListener('click', function() {
            if (currentPage > 1) {
                currentPage--;
                updatePagination();
            }
        });
        paginationControls.appendChild(prevButton);

        // Page number buttons
        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i;
            pageButton.disabled = i === currentPage; // Disable if it's the current page
            pageButton.addEventListener('click', function() {
                currentPage = i;
                updatePagination();
            });
            paginationControls.appendChild(pageButton);
        }

        // Next button
        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next';
        nextButton.disabled = currentPage === totalPages; // Disable if on the last page
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

    // Initialize
    updatePagination();

});
