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

/* Flèches pour replier / rouvrir le menu de gauche et la table des matières (choix mémorisé) */
(function () {
  var root = document.documentElement;
  function get(k) { try { return localStorage.getItem(k) === "1"; } catch (e) { return false; } }
  function set(k, v) { try { localStorage.setItem(k, v ? "1" : "0"); } catch (e) { } }
  function refresh() {
    var n = root.classList.contains("hide-nav"), t = root.classList.contains("hide-toc");
    var bn = document.getElementById("toggle-nav"), bt = document.getElementById("toggle-toc");
    if (bn) { bn.textContent = n ? "›" : "‹"; bn.title = n ? "Afficher le menu" : "Masquer le menu"; }
    if (bt) { bt.textContent = t ? "‹" : "›"; bt.title = t ? "Afficher la table des matières" : "Masquer la table des matières"; }
  }
  function make(id, cls, key) {
    if (document.getElementById(id)) return;
    var b = document.createElement("button"); b.id = id; b.type = "button"; b.className = "side-toggle";
    b.addEventListener("click", function () { var on = !root.classList.contains(cls); root.classList.toggle(cls, on); set(key, on); refresh(); });
    document.body.appendChild(b);
  }
  root.classList.toggle("hide-nav", get("hide-nav")); root.classList.toggle("hide-toc", get("hide-toc"));
  function mount() { make("toggle-nav", "hide-nav", "hide-nav"); make("toggle-toc", "hide-toc", "hide-toc"); refresh(); }
  if (window.document$) document$.subscribe(mount); else document.addEventListener("DOMContentLoaded", mount);
})();

/* Le simulateur s'ouvre toujours dans un nouvel onglet : on garde la page du TP sous la main */
(function () {
  function tag() {
    document.querySelectorAll('a[href*="simulateur-reseau.html"]').forEach(function (a) { a.target = "_blank"; a.rel = "noopener"; });
  }
  if (window.document$) document$.subscribe(tag); else document.addEventListener("DOMContentLoaded", tag);
})();
