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

/* Mode « projection » : texte agrandi, panneaux latéraux masqués. Bouton à côté du thème clair/foncé.
   Retour arrière : cliquer à nouveau (le choix est mémorisé dans le navigateur). */
(function () {
  var KEY = "projection-mode", root = document.documentElement;
  function get() { try { return localStorage.getItem(KEY) === "1"; } catch (e) { return false; } }
  function set(v) { try { localStorage.setItem(KEY, v ? "1" : "0"); } catch (e) { } }
  function apply(on, btn) {
    root.classList.toggle("projection", on);
    if (btn) { btn.setAttribute("aria-pressed", on ? "true" : "false"); btn.title = on ? "Quitter le mode projection" : "Mode projection (texte agrandi)"; }
  }
  function mount() {
    if (document.getElementById("projection-btn")) return;
    var pal = document.querySelector('[data-md-component="palette"]');
    var btn = document.createElement("button");
    btn.id = "projection-btn"; btn.type = "button"; btn.className = "md-header__button md-icon";
    btn.setAttribute("aria-label", "Mode projection");
    btn.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M2 4h20v12h-9v2h3v2H8v-2h3v-2H2V4m2 2v8h16V6H4m3 6 2.2-5h1.6L13 12h-1.5l-.4-1H8.9l-.4 1H7m2.3-2.2h1.4L10 8l-.7 1.8m5.2 2.2V7h1.5v5h-1.5Z"/></svg>';
    btn.addEventListener("click", function () { var on = !root.classList.contains("projection"); set(on); apply(on, btn); });
    if (pal && pal.parentNode) pal.parentNode.insertBefore(btn, pal.nextSibling); else { var h = document.querySelector(".md-header__inner"); if (h) h.appendChild(btn); }
    apply(get(), btn);
  }
  apply(get());
  if (window.document$) document$.subscribe(mount); else document.addEventListener("DOMContentLoaded", mount);
})();
