function renderPortfolio(allocation) {
    const allocationTable = document.querySelector("#portfolioTable tbody");
    allocationTable.innerHTML = ""; // Clear table

    allocation.forEach(item => {
        const row = `
            <tr>
                <td>${item.asset_class}</td>
                <td>${item.ticker}</td>
                <td>$${item.allocation.toFixed(2)}</td>
            </tr>`;
        allocationTable.innerHTML += row;
    });
}