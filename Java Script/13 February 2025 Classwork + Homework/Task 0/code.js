window.addEventListener(
    'load',
    main_function
);

function najal(kuda) {
    console.log("Я работаю! нажал (куда)");
    console.log(kuda);
}

function pomeniai_tsvet(event) {
    najal(kvadrat);
    console.log('clientX = ', event.clientX);
    console.log('pageX = ', event.pageX);
    console.log('screenX = ', event.screenX);
    console.log('clientY = ', event.clientY);
    console.log('pageY = ', event.pageY);
    console.log('screenY = ', event.screenY);
}

function pokraska() {
    // rgb(0, 0, 0) => rgb(255, 255, 255)
    // rgb(0, 180, 0) => rgb(255, 0, 255)
    // rgb(0, 0, 180) => rgb(0, 255, 255)
    // rgb(200, 100, 0) => rgb(255, 255, 0)
    let r = red_color.value;
    let g = 20;
    let b = 100;
    console.log(`rgb(${r}, ${g}, ${b})`);
    kvadrat.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
    // Правило! Если в CSS свойство пишется через дефис,
    // в JavaScript оно будет с больших букв (cameCase)
}

function main_function() {
    console.log('Страница готова');
    kvadrat.addEventListener(
        'click',
        pomeniai_tsvet
    );
    btn.addEventListener(
        'click',
        pokraska
    );
}