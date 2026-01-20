document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".cita-biblica").forEach(function (elemento) {
        elemento.addEventListener("click", function (e) {
            e.preventDefault();

            const clave = this.dataset.clave;

            fetch(`/biblia/${clave}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById("textoBiblico").innerText = data.texto;
                    document.getElementById("versionBiblica").innerText = data.version;

                    const modal = new bootstrap.Modal(
                        document.getElementById("bibliaModal")
                    );
                    modal.show();
                });
        });
    });
});
