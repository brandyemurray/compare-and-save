<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compare and Save</title>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background: white;
            padding: 30px 20px;
            margin-bottom: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .icon {
            font-size: 2em;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .tabs {
            display: flex;
            gap: 0;
            margin-bottom: 30px;
            border-bottom: 2px solid #ddd;
        }

        .tab-button {
            padding: 15px 30px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1em;
            color: #666;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
        }

        .tab-button.active {
            color: #2196F3;
            border-bottom-color: #2196F3;
        }

        .tab-button:hover {
            color: #333;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .form-section {
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .form-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: 600;
            margin-bottom: 8px;
            color: #333;
        }

        input, select {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1em;
            font-family: inherit;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #2196F3;
            box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
        }

        .products-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .products-table th {
            background: #f0f0f0;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #ddd;
        }

        .products-table td {
            padding: 12px;
            border-bottom: 1px solid #eee;
        }

        .products-table input {
            width: 100%;
            padding: 8px;
        }

        .products-table select {
            width: 100%;
            padding: 8px;
        }

        button {
            padding: 12px 30px;
            background: #d32f2f;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1em;
            cursor: pointer;
            transition: background 0.3s ease;
            font-weight: 600;
        }

        button:hover {
            background: #b71c1c;
        }

        button:active {
            transform: scale(0.98);
        }

        .info-box {
            background: #e3f2fd;
            border-left: 4px solid #2196F3;
            padding: 15px;
            margin-top: 20px;
            border-radius: 4px;
            color: #1565c0;
        }

        .info-box strong {
            display: block;
            margin-bottom: 10px;
            color: #0d47a1;
        }

        .info-box ol {
            margin-left: 20px;
            line-height: 1.8;
        }

        .preview-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 20px;
        }

        /* CARD DESIGN */
        .card-new {
            background: white;
            border: 3px solid #000;
            border-radius: 0;
            padding: 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            break-inside: avoid;
            page-break-inside: avoid;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .card-top {
            background: #f5f5f5;
            padding: 15px;
            border-bottom: 2px solid #000;
        }

        .card-title {
            font-size: 1.8em;
            font-weight: bold;
            margin-bottom: 8px;
            text-align: center;
            font-family: 'Cooper Black', Arial, sans-serif;
            letter-spacing: 2px;
        }

        .card-title .compare-save {
            font-size: 1.8em;
        }

        .card-title .and {
            font-size: 1.2em;
            margin: 0 8px;
        }

        .product-name-large {
            font-size: 1.6em;
            font-weight: bold;
            text-align: center;
            margin: 0;
        }

        .card-bottom {
            display: grid;
            grid-template-columns: 1fr 1fr;
            flex-grow: 1;
            padding: 0;
        }

        .left-column {
            padding: 20px;
            border-right: 2px solid #000;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .price-line {
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
        }

        .store-label {
            font-size: 0.9em;
            font-weight: 600;
            font-style: italic;
            color: #333;
            margin-bottom: 4px;
            font-family: 'Caveat', cursive;
            font-size: 1.2em;
        }

        .big-price {
            font-size: 1.8em;
            font-weight: bold;
            color: #000;
            font-family: Arial, sans-serif;
        }

        .date-line {
            font-size: 0.85em;
            color: #666;
            margin-top: 10px;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }

        .price-warning {
            font-size: 0.85em;
            color: #d32f2f;
            background: #ffebee;
            border: 1px solid #f44336;
            padding: 8px;
            border-radius: 3px;
            margin-top: 10px;
            font-weight: 600;
            text-align: center;
        }

        .right-column {
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #fff;
        }

        .savings-box {
            background: white;
            padding: 15px;
            text-align: center;
            width: 95%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .savings-text-arc {
            width: 140px;
            height: 70px;
            margin: 0 auto 5px;
            display: block;
        }

        .savings-big-amount {
            font-size: 2.8em;
            font-weight: bold;
            color: #d32f2f;
            line-height: 1;
            margin: 5px 0 0 0;
            font-family: Arial, sans-serif;
        }

        .savings-percent {
            font-size: 0.8em;
            color: #333;
            font-family: Arial, sans-serif;
            margin-top: 2px;
        }

        /* DNC CARD */
        .card-dnc {
            background: #ffebee;
            border: 3px solid #f44336;
            border-radius: 4px;
            padding: 20px;
            margin-bottom: 15px;
        }

        .dnc-header {
            font-size: 1.2em;
            font-weight: bold;
            color: #c62828;
            margin-bottom: 8px;
        }

        .dnc-text {
            font-size: 0.95em;
            color: #c62828;
        }

        .print-controls {
            text-align: center;
            margin-top: 30px;
        }

        .print-button {
            background: #1976d2;
            padding: 15px 40px;
            font-size: 1.1em;
        }

        .print-button:hover {
            background: #1565c0;
        }

        .no-results {
            text-align: center;
            padding: 40px;
            color: #666;
        }

        h3 {
            margin-top: 40px;
            color: #666;
            margin-bottom: 20px;
        }

        .warning-message {
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 4px;
            padding: 12px;
            margin-top: 10px;
            color: #856404;
            font-weight: 600;
        }

        @media print {
            body {
                background: white;
            }

            .container {
                max-width: 100%;
                padding: 0;
            }

            header, .tabs, .tab-button, .form-section, .print-controls, button {
                display: none;
            }

            .tab-content {
                display: block !important;
            }

            .card-new {
                border: 2px solid #000;
                margin-bottom: 0.3in;
                page-break-inside: avoid;
            }

            .preview-container {
                grid-template-columns: repeat(2, 1fr);
                gap: 0.3in;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>
                <span class="icon">💰</span>
                Compare and Save
            </h1>
            <p class="subtitle">Weekly Price Comparison Tool — Generate printable comparison cards</p>
        </header>

        <div class="tabs">
            <button class="tab-button active" data-tab="input">📋 Input Data</button>
            <button class="tab-button" data-tab="preview">👁️ Preview</button>
            <button class="tab-button" data-tab="print">🖨️ Print</button>
        </div>

        <!-- INPUT TAB -->
        <div id="input" class="tab-content active">
            <div class="form-section">
                <h2>Enter Product Prices</h2>
                
                <div id="inputWarnings"></div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="competitor">Which competitor?</label>
                        <select id="competitor">
                            <option value="Safeway/Albertsons">Safeway/Albertsons</option>
                            <option value="Winco">Winco</option>
                            <option value="Costco">Costco</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="checkDate">Price Check Date</label>
                        <input type="date" id="checkDate">
                    </div>
                    <div class="form-group">
                        <label for="productCount">How many products?</label>
                        <input type="number" id="productCount" value="2" min="1" max="50">
                    </div>
                </div>

                <h3 style="margin-top: 30px; margin-bottom: 15px;">Pricing Data</h3>
                <table class="products-table">
                    <thead>
                        <tr>
                            <th>Product Name</th>
                            <th>Super 1 Price</th>
                            <th>Competitor Price</th>
                            <th>Carries?</th>
                        </tr>
                    </thead>
                    <tbody id="productsBody">
                        <!-- Will be populated by JavaScript -->
                    </tbody>
                </table>

                <button onclick="generatePreview()">Generate Preview</button>

                <div class="info-box">
                    <strong>💡 How to use:</strong>
                    <ol>
                        <li>Enter product names and prices</li>
                        <li>Select 'DNC' (Does Not Carry) if the competitor doesn't have the item</li>
                        <li>Click "Generate Preview" to see how cards will look</li>
                        <li>Use the Print tab to print or export to PDF</li>
                    </ol>
                </div>
            </div>
        </div>

        <!-- PREVIEW TAB -->
        <div id="preview" class="tab-content">
            <div class="form-section">
                <div id="previewContent">
                    <p style="text-align: center; color: #999; padding: 40px;">
                        Click "Generate Preview" in the Input Data tab to see cards here
                    </p>
                </div>
            </div>
        </div>

        <!-- PRINT TAB -->
        <div id="print" class="tab-content">
            <div class="form-section">
                <div id="printContent">
                    <p style="text-align: center; color: #999; padding: 40px;">
                        Generate a preview first, then use this tab to print
                    </p>
                </div>
                <div class="print-controls">
                    <button class="print-button" onclick="window.print()">🖨️ Print / Export to PDF</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('checkDate').valueAsDate = new Date();

        document.querySelectorAll('.tab-button').forEach(button => {
            button.addEventListener('click', function() {
                const tabName = this.getAttribute('data-tab');
                
                document.querySelectorAll('.tab-content').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                document.querySelectorAll('.tab-button').forEach(btn => {
                    btn.classList.remove('active');
                });
                
                document.getElementById(tabName).classList.add('active');
                this.classList.add('active');
            });
        });

        document.getElementById('productCount').addEventListener('change', function() {
            updateProductsTable(parseInt(this.value));
        });

        function updateProductsTable(count) {
            const tbody = document.getElementById('productsBody');
            tbody.innerHTML = '';

            for (let i = 0; i < count; i++) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><input type="text" class="productName" placeholder="e.g., Milk" value="" onchange="checkWarnings()"></td>
                    <td><input type="number" class="super1Price" placeholder="3.99" step="0.01" value="" onchange="checkWarnings()"></td>
                    <td><input type="number" class="competitorPrice" placeholder="4.99" step="0.01" value="" onchange="checkWarnings()"></td>
                    <td>
                        <select class="carries">
                            <option value="Yes">Yes</option>
                            <option value="DNC">DNC</option>
                        </select>
                    </td>
                `;
                tbody.appendChild(row);
            }
        }

        function checkWarnings() {
            const rows = document.querySelectorAll('#productsBody tr');
            let warnings = [];
            
            rows.forEach((row, index) => {
                const name = row.querySelector('.productName').value.trim();
                const super1 = parseFloat(row.querySelector('.super1Price').value) || 0;
                const competitor = parseFloat(row.querySelector('.competitorPrice').value) || 0;
                
                if (name && super1 > 0 && competitor > 0 && super1 > competitor) {
                    warnings.push(`⚠️ ${name}: Super 1 price ($${super1.toFixed(2)}) is higher than competitor ($${competitor.toFixed(2)})`);
                }
            });
            
            const warningContainer = document.getElementById('inputWarnings');
            if (warnings.length > 0) {
                warningContainer.innerHTML = warnings.map(w => `<div class="warning-message">${w}</div>`).join('');
            } else {
                warningContainer.innerHTML = '';
            }
        }

        updateProductsTable(2);

        function generatePreview() {
            const products = [];
            const rows = document.querySelectorAll('#productsBody tr');
            
            rows.forEach(row => {
                const name = row.querySelector('.productName').value.trim();
                const super1Price = row.querySelector('.super1Price').value;
                const competitorPrice = row.querySelector('.competitorPrice').value;
                const carries = row.querySelector('.carries').value;
                
                if (name) {
                    products.push({
                        name: name,
                        super_one_price: super1Price ? parseFloat(super1Price) : 0,
                        competitor_price: competitorPrice ? parseFloat(competitorPrice) : 0,
                        carries: carries
                    });
                }
            });

            const competitor = document.getElementById('competitor').value;
            const date = document.getElementById('checkDate').value;

            fetch('/api/generate-cards', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    products: products,
                    competitor: competitor,
                    date: date
                })
            })
            .then(response => response.json())
            .then(data => {
                displayPreview(data);
                document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
                document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
                document.getElementById('preview').classList.add('active');
                document.querySelector('[data-tab="preview"]').classList.add('active');
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error generating preview. Check console.');
            });
        }

        function displayPreview(data) {
            let html = '';

            if (data.valid && data.valid.length > 0) {
                html += '<div class="preview-container">';
                
                data.valid.forEach((item, index) => {
                    const super1 = parseFloat(item.super_one_price);
                    const competitor = parseFloat(item.competitor_price);
                    const savings = (competitor - super1).toFixed(2);
                    const savingsPercent = Math.abs(((savings / competitor) * 100).toFixed(1));
                    const competitorName = data.competitor;
                    const date = data.date;
                    
                    const priceWarning = super1 > competitor;
                    const uniqueId = 'arc_' + Math.random().toString(36).substr(2, 9);
                    
                    html += `
                        <div class="card-new">
                            <div class="card-top">
                                <div class="card-title"><span class="compare-save">Compare</span> <span class="and">AND</span> <span class="compare-save">Save</span></div>
                                <div class="product-name-large">${item.name}</div>
                            </div>
                            
                            <div class="card-bottom">
                                <div class="left-column">
                                    <div class="price-line">
                                        <span class="store-label">${competitorName} Price</span>
                                        <span class="big-price">$${competitor.toFixed(2)}</span>
                                    </div>
                                    <div class="price-line">
                                        <span class="store-label">Super 1 Price</span>
                                        <span class="big-price">$${super1.toFixed(2)}</span>
                                    </div>
                                    <div class="date-line">Price Check Date: ${date}</div>
                                    ${priceWarning ? `<div class="price-warning">⚠️ Super 1 price is higher than ${competitorName}</div>` : ''}
                                </div>
                                
                                <div class="right-column">
                                    <div class="savings-box">
                                        <svg class="savings-text-arc" viewBox="0 0 250 120" preserveAspectRatio="xMidYMid meet">
                                            <defs>
                                                <path id="arcPath_${uniqueId}" d="M 30,100 A 90,90 0 0,1 220,100" fill="none" stroke="none"/>
                                            </defs>
                                            <text font-family="Arial, sans-serif" font-size="18" font-weight="bold" letter-spacing="3" fill="#000">
                                                <textPath href="#arcPath_${uniqueId}" startOffset="50%" text-anchor="middle">
                                                    BUYING POWER SAVINGS
                                                </textPath>
                                            </text>
                                        </svg>
                                        <div class="savings-big-amount">$${Math.abs(savings)}</div>
                                        <div class="savings-percent">(${savingsPercent}% savings)</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                });
                
                html += '</div>';
            }

            if (data.dnc && data.dnc.length > 0) {
                html += '<h3>Does Not Carry Items:</h3>';
                data.dnc.forEach(item => {
                    html += `
                        <div class="card-dnc">
                            <div class="dnc-header">❌ ${item.name}</div>
                            <div class="dnc-text">${data.competitor} does not carry this item</div>
                        </div>
                    `;
                });
            }

            if (!data.valid || data.valid.length === 0) {
                html += '<div class="no-results"><p>No valid comparisons to display.</p><p>Make sure you have entered both prices (not 0).</p></div>';
            }

            document.getElementById('previewContent').innerHTML = html;
            document.getElementById('printContent').innerHTML = html + `
                <div class="print-controls">
                    <button class="print-button" onclick="window.print()">🖨️ Print / Export to PDF</button>
                </div>
            `;
        }
    </script>
</body>
</html>
