field = document.getElementById('phone-mask')
field.addEventListener('focus', (e) => {
    if (e.target.id && !field.value) {
        field.value = '+375('
        var phoneMask = IMask(
            document.getElementById('phone-mask'), {
                mask: '+{375}(00)000-00-00'
            });
    }
})
