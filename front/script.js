document.addEventListener("DOMContentLoaded", function () {
    fetch("http://localhost:8000/cursos/")
        .then(response => {
            if (response.status > 400) {
                throw new Error('Erro ao carregar cursos:', response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log(typeof data)
            console.log(data)
            const cursosLista = document.getElementById("cursos-lista");
            
            // Convertendo as propriedades numeradas em um array
            const cursosArray = Object.keys(data).map(key => data[key]);
            
            // cursosArray.forEach(curso => {
            //     const itemLista = document.createElement("h2");
            //     itemLista.textContent = curso.descricao;
            //     cursosLista.appendChild(itemLista);
            // });
            cursosArray.forEach(curso => {
                const itemLista = document.createElement("h2");
                itemLista.innerHTML = `<strong>${curso.codigo}</strong>: ${curso.descricao} (Nível ${curso.nivel})`;
                cursosLista.appendChild(itemLista);
            });
        })
        .catch(error => console.error(error));
});
