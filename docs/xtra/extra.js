/* Pastilles d'autonomie et boutons « Ouvrir » dans les tableaux de progression */
function decorate() {
  document.querySelectorAll(".md-typeset table td").forEach(function (td) {
    var t = td.textContent.trim();
    if (t === "🟢 Guidé") td.innerHTML = '<span class="pill pill-g">Guidé</span>';
    else if (t === "🟡 Semi-guidé") td.innerHTML = '<span class="pill pill-y">Semi-guidé</span>';
    else if (t === "🔴 Autonome") td.innerHTML = '<span class="pill pill-r">Autonome</span>';
    else if (t === "🚧 en préparation") td.innerHTML = '<span class="soon">🚧 en préparation</span>';
    else { var a = td.querySelector("a"); if (a && a.textContent.indexOf("Ouvrir") >= 0 && td.children.length === 1) { a.className = "btn-open"; a.textContent = "Ouvrir →"; } }
  });
}
if (window.document$) document$.subscribe(decorate); else document.addEventListener("DOMContentLoaded", decorate);
