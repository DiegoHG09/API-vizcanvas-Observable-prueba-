---
title: Directorio de fuentes (Cards)
---

# Directorio de fuentes (Cards)

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
html`<p class="contador">
  Mostrando <strong>${datosFiltrados.length}</strong> de
  <strong>${directorio.length}</strong> fuentes
</p>`
```

```js
datosFiltrados.length === 0
  ? html`<p class="sin-resultados">No se encontraron fuentes con los filtros seleccionados.</p>`
  : html`<div class="cards-grid">
      ${datosFiltrados
        .filter(d => d.Nombre_de_la_fuente?.trim())
        .map(d => html`<article class="fuente-card">
          ${d.categoria ? html`<span class="badge">${d.categoria}</span>` : ''}
          ${d.Nombre_de_la_fuente ? html`<h3 class="card-titulo">${d.Nombre_de_la_fuente}</h3>` : ''}
          ${(d.Tipo_de_fuente || d.Año_referencia || d.Nivel_de_desagregación)
            ? html`<div class="card-meta">
                ${d.Tipo_de_fuente ? html`<span class="chip">${d.Tipo_de_fuente}</span>` : ''}
                ${d.Año_referencia != null ? html`<span class="chip">${String(d.Año_referencia)}</span>` : ''}
                ${d.Nivel_de_desagregación ? html`<span class="chip">${d.Nivel_de_desagregación}</span>` : ''}
              </div>` : ''}
          ${d.Cont_inf_indigena ? html`<p class="card-contenido">${d.Cont_inf_indigena}</p>` : ''}
          ${d.Notas ? html`<p class="card-nota">${d.Notas}</p>` : ''}
          ${d.URL ? html`<div class="card-footer">
              <a href="${d.URL}" target="_blank" class="card-link">Ver fuente →</a>
            </div>` : ''}
        </article>`)}
    </div>`
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
    margin: 0 0 1rem;
  }

  .sin-resultados {
    color: var(--theme-foreground-muted);
    font-style: italic;
    text-align: center;
    padding: 3rem 0;
  }

  .cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 1.25rem;
  }

  .fuente-card {
    background: var(--theme-background-alt);
    border: 1px solid var(--theme-foreground-faintest);
    border-radius: 8px;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
  }

  .badge {
    display: inline-block;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--theme-foreground-muted);
    background: var(--theme-background);
    border: 1px solid var(--theme-foreground-faintest);
    border-radius: 4px;
    padding: 0.2em 0.55em;
    width: fit-content;
  }

  .card-titulo {
    font-size: 0.975rem;
    font-weight: 600;
    margin: 0;
    line-height: 1.4;
    color: var(--theme-foreground);
  }

  .card-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .chip {
    font-size: 0.72rem;
    color: var(--theme-foreground-muted);
    background: var(--theme-background);
    border: 1px solid var(--theme-foreground-faintest);
    border-radius: 20px;
    padding: 0.2em 0.7em;
  }

  .card-contenido {
    font-size: 0.855rem;
    color: var(--theme-foreground-alt);
    margin: 0;
    line-height: 1.55;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .card-nota {
    font-size: 0.78rem;
    color: var(--theme-foreground-muted);
    margin: 0;
    padding: 0.6rem 0.75rem;
    background: var(--theme-background);
    border-left: 3px solid var(--theme-foreground-faintest);
    border-radius: 0 4px 4px 0;
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .card-footer {
    display: flex;
    justify-content: flex-end;
    margin-top: auto;
    padding-top: 0.5rem;
  }

  .card-link {
    font-size: 0.855rem;
    font-weight: 500;
    color: var(--theme-foreground-focus);
    text-decoration: none;
  }

  .card-link:hover {
    text-decoration: underline;
  }
</style>