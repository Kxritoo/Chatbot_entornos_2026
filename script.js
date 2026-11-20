const prompt = "Hola, ¿qué es la inteligencia artificial?"
const res = await fetch("http://localhost:8000/chat/" + prompt)
console.log(prompt)
const datos = await res.json()

console.log(datos)