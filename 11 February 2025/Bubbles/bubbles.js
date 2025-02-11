function createBubble() {
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = '🎈';          // надеюсь эмодзи можно)

    bubble.addEventListener('click', () => {
        bubble.style.display = 'none'; 
    });
    document.body.appendChild(bubble);
}

for (let i = 0; i < 10; i++) {         // можно ли как-то сделать рандомно генерируемое число?
    createBubble();
}