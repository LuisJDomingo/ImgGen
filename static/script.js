document.getElementById("profile-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;

    const response = await fetch("/save_profile", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description })
    });

    const result = await response.json();
    alert(result.message);
});

document.getElementById("scene-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const scene = document.getElementById("scene").value;

    const response = await fetch("/generate_image", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ scene })
    });

    const result = await response.json();
    document.getElementById("result").innerHTML = `<img src="${result.image_url}" alt="Imagen Generada">`;
});
