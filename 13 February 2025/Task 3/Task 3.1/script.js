function changeBackgroundColor() {
    document.body.style.backgroundColor = 'lightblue';
}

document.getElementById('paintLink').addEventListener('click', function() {
    changeBackgroundColor();
});