function calculateBMI() {
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    if (weight > 0 && height > 0) {
        const bmi = (weight / ((height / 100) ** 2)).toFixed(2);
        let result = `Your BMI is ${bmi}`;

        if (bmi < 18.5) {
            result += " (Underweight)";
        } else if (bmi >= 18.5 && bmi < 24.9) {
            result += " (Normal weight)";
        } else if (bmi >= 25 && bmi < 29.9) {
            result += " (Overweight)";
        } else {
            result += " (Obese)";
        }

        document.getElementById('result').innerText = result;
    } else {
        document.getElementById('result').innerText = "Please enter valid values.";
    }
}
