function Selection() {
    const shoeType = document.querySelector('input[name="shoeType"]:checked');
    const shoeSize = document.querySelector('input[name="shoeSize"]:checked');

    if (shoeType && shoeSize) {
        alert(`Вы выбрали: ${shoeType.value} размер ${shoeSize.value}`);
    } else {
        alert('Пожалуйста, выберите тип обуви и размер.');
    }
}