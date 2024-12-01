document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.button-animal.favoritar').addEventListener('click', function() {
        var button = this;
        var animalId = "{{ animal.id }}";
        var csrftoken = '{{ csrf_token }}';

        fetch(`{% url "adoptions:toggle_favorite" animal.id %}`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({}),
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_favorited) {
                button.innerHTML = '<i class="fa-solid fa-heart-crack"></i><p>Tirar {% if animal.nome %} {{animal.nome}} {% endif %} dos favoritos</p>';
            } else {
                button.innerHTML = '<i class="fa-solid fa-heart"></i><p>Favoritar {% if animal.nome %} {{animal.nome}} {% endif %}</p>';
            }
        });
    });
});

