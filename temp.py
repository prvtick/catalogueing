import pandas as pd

# Load the Excel file
df = pd.read_excel('C:/Users/manda/OneDrive/Desktop/medijini/B2B Product Category1.xlsx')

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Print column names to verify
print("Columns in the DataFrame:", df.columns)

# Group products by category
grouped_products = df.groupby('Category')

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Products Catalog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fff;
            color: #333;
            margin: 0;
            padding: 0;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        body.dark-mode {
            background-color: #121212;
            color: #e0e0e0;
        }
        header {
            background-color: #2952a3;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            color: #fff;
            margin: 0;
        }
        .search-bar {
            margin: 20px auto;
            width: 50%;
            display: flex;
            justify-content: center;
        }
        .search-bar input {
            width: 60%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 20px 0 0 20px;  /* Rounded input */
            background-color: #fff;
            color: #333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .search-bar input.dark-mode {
            background-color: #333;
            color: #fff;
            border: 1px solid #555;
        }
        .search-bar button {
            width: 20%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            background-color: #2952a3;
            color: #fff;
            border-radius: 0 20px 20px 0;  /* Rounded button */
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .search-bar button.dark-mode {
            background-color: #2952a3;
            border: 1px solid #444;
        }
        .search-bar button:hover {
            background-color: #1E90FF;
            transform: scale(1.05);
        }
        .search-bar button.clear-button {
            background-color: #404040;
            margin-left: 10px;
            padding: 5px 10px;
            font-size: 14px;
            width: auto;
        }
        .search-bar button.clear-button.dark-mode {
            background-color: #666;
        }
        .search-bar button.clear-button:hover {
            background-color: #ff4500;
        }
        .filters {
            margin: 20px;
            display: flex;
            justify-content: center;
        }
        .filters select {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 20px;  /* Rounded select */
            background-color: #fff;
            color: #333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .filters select.dark-mode {
            background-color: #333;
            color: #fff;
            border: 1px solid #555;
        }
        .product-category {
            margin: 20px;
        }
        .product-category h2 {
            color: #2952a3;
            border-bottom: 2px solid #2952a3;
            padding-bottom: 10px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .product-category h2:hover {
            background-color: #2952a3;
            color: #fff;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 0 20px;
        }
        .product-card {
            display: flex;
            flex-direction: column;
            border: 1px solid #ccc;
            border-radius: 20px;  /* Rounded card */
            overflow: hidden;
            background-color: #fff;
            transition: box-shadow 0.3s ease, transform 0.3s ease, background-color 0.3s ease;
            min-height: 400px;
            position: relative;
        }
        .product-card.dark-mode {
            background-color: #1e1e1e;
            border: 1px solid #555;
        }
        .product-card:hover {
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }
        .product-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        .product-card img:hover {
            transform: scale(1.1);
        }
        .card-content {
            display: flex;
            flex-direction: column;
            height: 100%;
            padding: 15px;
            box-sizing: border-box;
        }
        .card-content h3 {
            margin-top: 0;
            color: #333;
            font-size: 18px;
            transition: color 0.3s ease;
        }
        .card-content h3.dark-mode {
            color: #e0e0e0;
        }
        .card-content p {
            margin: 10px 0;
            color: #555;
            font-size: 14px;
        }
        .card-content .price {
            color: #2952a3;
            font-weight: bold;
            font-size: 16px;
        }
        .card-content .brand {
            font-size: 12px;
            color: #777;
        }
        .card-content button {
            width: 100%;
            padding: 10px;
            background-color: #2952a3;
            color: #fff;
            border: none;
            border-radius: 0 0 20px 20px;  /* Rounded button */
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .card-content button:hover {
            background-color: #1E90FF;
            transform: scale(1.05);
        }
        .expandable-content {
            overflow: hidden;
            transition: max-height 0.5s ease;
            max-height: 0;
        }
        .expandable-content.show {
            max-height: 500px; /* Adjust as needed */
        }
        .card-content .more-info {
            font-size: 14px;
            color: #333;
            cursor: pointer;
            text-align: center;
            margin-top: auto;
            transition: color 0.3s ease;
        }
        .card-content .more-info:hover {
            color: #2952a3;
        }
        .dark-mode-button {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: #001a4d;
            color: #fff;
            border: none;
            border-radius: 20px;  /* Rounded button */
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .dark-mode-button.dark-mode {
            background-color: #1e1e1e;
            color: #e0e0e0;
        }
        .dark-mode-button:hover {
            background-color: #1E90FF;
            transform: scale(1.05);
        }
    </style>
    <script>
        function filterProducts() {
            const searchInput = document.getElementById("searchInput").value.toLowerCase();
            const categoryFilter = document.getElementById("categoryFilter").value.toLowerCase();
            const products = document.getElementsByClassName("product-card");

            Array.from(products).forEach(product => {
                const productName = product.querySelector("h3").innerText.toLowerCase();
                const productCategory = product.getAttribute("data-category").toLowerCase();
                product.style.display = (productName.includes(searchInput) || !searchInput) &&
                                         (productCategory.includes(categoryFilter) || categoryFilter === "all")
                                         ? ""
                                         : "none";
            });
        }

        function clearSearch() {
            document.getElementById("searchInput").value = "";
            filterProducts();  // Reapply the filter with an empty search term
        }

        function toggleExpand(id) {
            const expandableContent = document.getElementById(id);
            const moreInfo = document.getElementById("more-info-" + id);
            const isExpanded = expandableContent.classList.contains('show');

            expandableContent.classList.toggle('show', !isExpanded);
            expandableContent.classList.toggle('hidden', isExpanded);
            moreInfo.innerText = isExpanded ? "Read More" : "Read Less";
            moreInfo.setAttribute("aria-expanded", !isExpanded);
        }

        function toggleDarkMode() {
            const body = document.body;
            const darkMode = body.classList.toggle('dark-mode');
            document.querySelectorAll('.search-bar input, .search-bar button, .filters select').forEach(element => {
                element.classList.toggle('dark-mode', darkMode);
            });
            document.querySelectorAll('.product-card').forEach(card => {
                card.classList.toggle('dark-mode', darkMode);
                card.querySelector('h3').classList.toggle('dark-mode', darkMode);
            });
            document.querySelector('.dark-mode-button').innerText = darkMode ? 'Light Mode' : 'Dark Mode';
            localStorage.setItem('dark-mode', darkMode);
        }

        document.addEventListener('DOMContentLoaded', () => {
            const darkMode = localStorage.getItem('dark-mode') === 'true';
            if (darkMode) {
                document.body.classList.add('dark-mode');
                document.querySelectorAll('.search-bar input, .search-bar button, .filters select').forEach(element => {
                    element.classList.add('dark-mode');
                });
                document.querySelectorAll('.product-card').forEach(card => {
                    card.classList.add('dark-mode');
                    card.querySelector('h3').classList.add('dark-mode');
                });
                document.querySelector('.dark-mode-button').innerText = 'Light Mode';
            } else {
                document.querySelector('.dark-mode-button').innerText = 'Dark Mode';
            }
        });
    </script>
</head>
<body>

<header>
    <h1>MediJini Product Catalog</h1>
</header>

<div class="search-bar">
    <input type="text" id="searchInput" placeholder="Search for products..." onkeyup="filterProducts()">
    <button onclick="filterProducts()">Search</button>
    <button onclick="clearSearch()" class="clear-button">Clear</button>
</div>

<div class="filters">
    <select id="categoryFilter" onchange="filterProducts()">
        <option value="all">All Categories</option>
"""

# Adding category options dynamically
categories = grouped_products.groups.keys()
html_template += "".join(f"<option value='{category}'>{category}</option>" for category in categories)

html_template += """
    </select>
</div>

<button class="dark-mode-button" onclick="toggleDarkMode()">Dark Mode</button>
"""

# Adding products dynamically by category
for category, items in grouped_products:
    html_template += f"<div class='product-category'><h2>{category}</h2><div class='product-grid'>"
    
    for index, item in items.iterrows():
        product_name = item['Products']
        brand = item['Brand'] if not pd.isna(item['Brand']) else 'Unknown Brand'
        specification = item.get('Specification', 'No Specification Available')
        image_url = item.get('ImageURL', 'placeholder.jpg')  # Use placeholder if image URL is missing

        expandable_id = f"expandable-{index}"

        html_template += f"""
        <div class='product-card' data-category='{category}'>
            <img src='{image_url}' alt='{product_name}'>
            <div class='card-content'>
                <h3>{product_name}</h3>
                <p class='brand'>{brand}</p>
                <p class='price'>Price</p>
                <div class='expandable-content hidden' id='{expandable_id}' aria-hidden='true'>
                    {specification}
                </div>
                <div class='more-info' id='more-info-{expandable_id}' onclick='toggleExpand("{expandable_id}")' aria-expanded='false'>
                    Read More
                </div>
                <button>Add to Cart</button>
            </div>
        </div>"""
    
    html_template += "</div></div>"

html_template += "</body></html>"

# Save the HTML to a file with UTF-8 encoding
with open('C:/Users/manda/OneDrive/Desktop/medijini/catalog.html', 'w', encoding='utf-8') as file:
    file.write(html_template)
