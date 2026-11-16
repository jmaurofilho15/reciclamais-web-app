document.addEventListener("DOMContentLoaded", function() {
    // Gestão visual dos cards de materiais
    const cards = document.querySelectorAll(".material-card");
    
    cards.forEach(card => {
        const radio = card.querySelector('input[type="radio"]');
        
        if (radio && radio.checked) {
            card.classList.add("selected");
        }

        card.addEventListener("click", function() {
            cards.forEach(c => c.classList.remove("selected"));
            this.classList.add("selected");
            if (radio) {
                radio.checked = true;
            }
        });
    });

    // Máscara para Telefone: (00) 00000-0000
    const telInput = document.getElementById("telefone");
    if (telInput) {
        telInput.addEventListener("input", function(e) {
            let value = e.target.value.replace(/\D/g, "");
            if (value.length > 11) value = value.slice(0, 11);
            
            if (value.length > 6) {
                value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7)}`;
            } else if (value.length > 2) {
                value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length > 0) {
                value = `(${value}`;
            }
            e.target.value = value;
        });
    }

    // Máscara para CEP: 00000-000
    const cepInput = document.getElementById("cep");
    if (cepInput) {
        cepInput.addEventListener("input", function(e) {
            let value = e.target.value.replace(/\D/g, "");
            if (value.length > 8) value = value.slice(0, 8);
            
            if (value.length > 5) {
                value = `${value.slice(0, 5)}-${value.slice(5)}`;
            }
            e.target.value = value;
        });
    }
});