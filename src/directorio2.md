---
title: Directorio (prueba)
draft: true
---

# Directorio (prueba)

```js
const directorio = FileAttachment("data/directorio.csv").csv({typed: true})
```

```js
const temas = ["Todos", ...new Set(
  directorio
    .filter(d => d.Tema)
    .flatMap(d => d.Tema.split(",").map(s => s.trim()))
)]

const temaSeleccionado = view(Inputs.select(temas, {label: "Tema"}))
```

```js
const datosFiltrados = temaSeleccionado === "Todos"
  ? directorio
  : directorio.filter(d => d.Tema && d.Tema.split(",").map(s => s.trim()).includes(temaSeleccionado))
```

```js
Inputs.table(datosFiltrados, {
  rows: 35,
  columns: temaSeleccionado === "Todos"
    ? ["Nombre_de_la_fuente", "Tema", "Tipo_de_fuente", "Año_referencia", "Cont_inf_indigena", "URL"]
    : ["Nombre_de_la_fuente", "Tipo_de_fuente", "Año_referencia", "Cont_inf_indigena", "URL"],
  width: {
    Nombre_de_la_fuente: 220,
    Tipo_de_fuente: 90,
    Año_referencia: 80,
    Cont_inf_indigena: 260,
    URL: 110
  },
  format: {
    Año_referencia: d => d != null ? String(d) : "",
    URL: url => url ? Object.assign(document.createElement("a"), {
      href: url,
      textContent: "Ver fuente →",
      target: "_blank"
    }) : ""
  }
})
```
<style>
  :root {
    --theme-width-normal: 95%;
    --theme-width-medium: 95%;
  }
</style>