function calculateTotal() {
    const costPerLiter = parseFloat(document.getElementById('petrolCost').value);
    const liters = parseFloat(document.getElementById('liters').value);

    const totalCost = costPerLiter * liters;

    document.getElementById('result').textContent = 
        `$${totalCost.toFixed(2)}`;
}
