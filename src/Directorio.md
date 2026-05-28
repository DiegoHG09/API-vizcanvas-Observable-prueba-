---
title: Directorio de fuentes (Tabla)
---

# Directorio de fuentes (Tabla)

```js
const directorio = FileAttachment("data/directorio.csv").csv({typed: true})
```

<div class="panel-filtros">
<h3>Buscar y filtrar</h3>

```js
const busqueda = view(Inputs.search(directorio, {
  placeholder: "Buscar por nombre, contenido, institución..."
}))
```

```js
const temas = ["Todos", ...new Set(
  busqueda
    .filter(d => d.Tema)
    .flatMap(d => d.Tema.split(",").map(s => s.trim()))
)]
const temaSeleccionado = view(Inputs.select(temas, {label: "Tema"}))
```

```js
const subtemas = ["Todos", ...new Set(
  busqueda
    .filter(d => d.Subtema && (temaSeleccionado === "Todos" || 
      (d.Tema && d.Tema.split(",").map(s => s.trim()).includes(temaSeleccionado))))
    .flatMap(d => d.Subtema.split(",").map(s => s.trim()))
)]
const subtemaSeleccionado = view(Inputs.select(subtemas, {label: "Subtema"}))
```

</div>

```js
const datosFiltrados = busqueda
  .filter(d => temaSeleccionado === "Todos" || 
    (d.Tema && d.Tema.split(",").map(s => s.trim()).includes(temaSeleccionado)))
  .filter(d => subtemaSeleccionado === "Todos" || 
    (d.Subtema && d.Subtema.split(",").map(s => s.trim()).includes(subtemaSeleccionado)))
```

```js
html`<p class="contador">Mostrando <strong>${datosFiltrados.length}</strong> de <strong>${directorio.length}</strong> fuentes</p>`
```

```js
Inputs.table(datosFiltrados, {
  rows: 30,
  columns: temaSeleccionado === "Todos"
    ? ["Nombre_de_la_fuente", "Tema", "Tipo_de_fuente", "Año_referencia", "Cont_inf_indigena", "URL"]
    : ["Nombre_de_la_fuente", "Tipo_de_fuente", "Año_referencia", "Cont_inf_indigena", "URL"],
  header: {
    Nombre_de_la_fuente: "Fuente",
    Tema: "Tema",
    Tipo_de_fuente: "Tipo",
    Año_referencia: "Año",
    Cont_inf_indigena: "Contenido sobre población indígena",
    URL: "Acceso"
  },
  width: {
    Nombre_de_la_fuente: 220,
    Tipo_de_fuente: 90,
    Año_referencia: 60,
    Cont_inf_indigena: 280,
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

  .panel-filtros {
    background: var(--theme-background-alt);
    border: 1px solid var(--theme-foreground-faintest);
    border-radius: 8px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.5rem;
  }

  .panel-filtros h3 {
    margin: 0 0 1rem 0;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--theme-foreground-muted);
  }

  .contador {
    font-size: 0.875rem;
    color: var(--theme-foreground-muted);
    margin: 0.75rem 0 0.25rem;
  }
</style>