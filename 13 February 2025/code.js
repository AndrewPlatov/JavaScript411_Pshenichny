
window.addEventListener(
    'load',
    main_function
);

function najal(kuda) {
    console.log('Im working!')
    console.log(kuda);
}

function pomeniai_tsvet(event) {
    najal(kvadrat)
    console.log('clientX = ', event.clientX);
    console.log('pageX = ', event.pageX);
    console.log('screenX = ', event.screenX);
    console.log('clientY = ', event.clientX);
    console.log('pageY = ', event.pageY);
    console.log('screenY = ', event.screenY);
}

function main_function() {
    console.log('Page is ready');
    kvadrat.addEventListener(
        'click',
        (event) => {
            najal(kvadrat);
        }
    );
}