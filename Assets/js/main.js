(function () {
  "use strict";

  var doc = document.documentElement;
  var lang = doc.lang === "en" ? "en" : "ml";
  var SITE = window.SITE || { videos: [] };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var T = {
    ml: {
      soon: "ലിങ്ക് ഉടൻ ചേർക്കും",
      noVideos: "വീഡിയോകൾ ഉടൻ ചേർക്കും",
      of: " / ",
      items: "എണ്ണം",
      video: "വീഡിയോ"
    },
    en: {
      soon: "Link coming soon",
      noVideos: "Videos will be added soon",
      of: " / ",
      items: "items",
      video: "Video"
    }
  }[lang];

  function $(s, el) { return (el || document).querySelector(s); }
  function $$(s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); }

  /* ---------- Theme ---------- */
  var themeBtn = $(".theme-btn");
  function currentTheme() {
    var t = doc.getAttribute("data-theme");
    if (t) return t;
    return "light";
  }
  function syncThemeMeta() {
    var m = $('meta[name="theme-color"]:not([media])');
    if (m) m.setAttribute("content", currentTheme() === "dark" ? "#050506" : "#f3f6fb");
  }
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      doc.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      syncThemeMeta();
    });
  }
  syncThemeMeta();

  /* ---------- Language preference ---------- */
  $$(".lang, [data-lang-link]").forEach(function (a) {
    a.addEventListener("click", function () {
      try { localStorage.setItem("lang", a.getAttribute("hreflang") || ""); } catch (e) {}
    });
  });

  /* ---------- Header ---------- */
  var header = $(".header");
  var toTop = $(".to-top");
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var y = window.scrollY;
      header && header.classList.toggle("is-scrolled", y > 8);
      toTop && toTop.classList.toggle("is-visible", y > 900);
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  toTop && toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* Mobile menu */
  var menuBtn = $(".menu-btn");
  function setMenu(open) {
    doc.classList.toggle("menu-open", open);
    menuBtn && menuBtn.setAttribute("aria-expanded", String(open));
  }
  menuBtn && menuBtn.addEventListener("click", function () { setMenu(!doc.classList.contains("menu-open")); });
  $$(".sheet a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* Active nav link */
  var navLinks = $$(".nav a[href^='#']");
  if ("IntersectionObserver" in window && navLinks.length) {
    var map = {};
    navLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          navLinks.forEach(function (a) { a.classList.remove("is-active"); });
          map[en.target.id].classList.add("is-active");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); el && spy.observe(el); });
  }

  /* ---------- Reveal + count up ---------- */
  function countUp(el) {
    var end = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce || !end) { el.textContent = end + suffix; return; }
    var start = null, dur = 900;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        $$("[data-count]", en.target).forEach(countUp);
        if (en.target.hasAttribute("data-count")) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- Social links from config ---------- */
  $$("[data-link]").forEach(function (a) {
    var url = SITE[a.getAttribute("data-link")];
    if (url) {
      a.href = url;
    } else if (a.getAttribute("href") === "#") {
      a.classList.add("is-pending");
      a.setAttribute("aria-disabled", "true");
      a.removeAttribute("href");
      var v = $("[data-link-value]", a);
      if (v) v.textContent = T.soon;
    }
  });

  /* ---------- Videos from config ---------- */
  function ytId(s) {
    if (!s) return "";
    var m = String(s).match(/(?:youtu\.be\/|v=|embed\/|shorts\/|live\/)([\w-]{11})/);
    return m ? m[1] : (/^[\w-]{11}$/.test(s) ? s : "");
  }
  var vPanel = $("#panel-videos");
  var videos = (SITE.videos || []).map(function (v) { return { id: ytId(v.id), title: v[lang] || v.ml || v.en || T.video }; }).filter(function (v) { return v.id; });
  if (vPanel && !vPanel.children.length) {
    if (!videos.length) {
      vPanel.innerHTML = '<div class="empty"><svg class="icon" aria-hidden="true"><use href="#i-youtube"/></svg><p>' + T.noVideos + "</p></div>";
    } else {
      var html = '<div class="grid grid--video">';
      videos.forEach(function (v, i) {
        html += '<button type="button" class="tile video-tile" style="--i:' + i + '" data-yt="' + v.id + '" data-cap="' + v.title.replace(/"/g, "&quot;") + '">' +
          '<img loading="lazy" decoding="async" width="480" height="270" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt="' + v.title.replace(/"/g, "&quot;") + '">' +
          '<span class="play"><span><svg class="icon icon--fill" aria-hidden="true"><use href="#i-play"/></svg></span></span>' +
          "<figcaption>" + v.title + "</figcaption></button>";
      });
      vPanel.innerHTML = html + "</div>";
    }
  }

  /* ---------- Load-in ---------- */
  requestAnimationFrame(function () { requestAnimationFrame(function () { doc.classList.add("is-loaded"); }); });

  /* ---------- Scroll-linked effects ---------- */
  var progress = $(".progress");
  var bandRows = $$(".band__row");
  var band = $(".band");
  var portraitImg = $(".portrait__frame img");
  var timeline = $(".timeline");
  var tItems = timeline ? $$("li", timeline) : [];
  var sTick = false;
  function onScrollFx() {
    sTick = false;
    var y = window.scrollY, vh = window.innerHeight;
    var max = document.documentElement.scrollHeight - vh;
    var p = max > 0 ? Math.min(1, y / max) : 0;
    doc.style.setProperty("--p", p.toFixed(4));
    if (reduce) return;

    // Phase 1: Batch all DOM layout reads first (prevents forced reflow)
    var bandActive = false, bandOff = 0;
    if (band) {
      var r = band.getBoundingClientRect();
      if (r.bottom > 0 && r.top < vh) {
        bandActive = true;
        bandOff = (vh - r.top);
      }
    }
    var tpVal = null, reachedFlags = [];
    if (timeline) {
      var tr = timeline.getBoundingClientRect();
      tpVal = Math.max(0, Math.min(1, (vh * 0.65 - tr.top) / tr.height)).toFixed(3);
      for (var i = 0; i < tItems.length; i++) {
        reachedFlags.push(tItems[i].getBoundingClientRect().top + 10 < vh * 0.65);
      }
    }

    // Phase 2: Batch all DOM writes together
    if (bandActive) {
      bandRows.forEach(function (row) {
        var sp = parseFloat(row.getAttribute("data-speed")) || 0.2;
        var base = sp < 0 ? 0 : -row.scrollWidth / 3;
        row.style.transform = "translate3d(" + (base + bandOff * sp) + "px,0,0)";
      });
    }
    if (portraitImg && y < vh * 1.2) {
      portraitImg.style.setProperty("--py", (y * 0.06).toFixed(1) + "px");
    }
    if (timeline && tpVal !== null) {
      timeline.style.setProperty("--tp", tpVal);
      for (var j = 0; j < tItems.length; j++) {
        tItems[j].classList.toggle("is-reached", reachedFlags[j]);
      }
    }
  }
  function reqFx() { if (!sTick) { sTick = true; requestAnimationFrame(onScrollFx); } }
  window.addEventListener("scroll", reqFx, { passive: true });
  window.addEventListener("resize", reqFx);
  onScrollFx();

  /* ---------- Pointer effects (mouse / pen only) ---------- */
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (fine && !reduce) {
    document.addEventListener("pointermove", function (e) {
      var s = e.target.closest && e.target.closest(".spot, .portrait");
      if (!s) return;
      var r = s.getBoundingClientRect();
      s.style.setProperty("--mx", (e.clientX - r.left) + "px");
      s.style.setProperty("--my", (e.clientY - r.top) + "px");
    }, { passive: true });

    var portrait = $(".portrait");
    var tilt = $(".portrait__tilt");
    if (portrait && tilt) {
      portrait.addEventListener("pointermove", function (e) {
        var r = portrait.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var yy = (e.clientY - r.top) / r.height - 0.5;
        tilt.style.transform = "rotateY(" + (x * 10).toFixed(2) + "deg) rotateX(" + (-yy * 10).toFixed(2) + "deg)";
      });
      portrait.addEventListener("pointerleave", function () { tilt.style.transform = ""; });
    }
  }

  /* Ripple on buttons */
  document.addEventListener("pointerdown", function (e) {
    var b = e.target.closest && e.target.closest(".btn");
    if (!b || reduce) return;
    var r = b.getBoundingClientRect();
    var d = Math.max(r.width, r.height);
    var s = document.createElement("span");
    s.className = "ripple";
    s.style.width = s.style.height = d + "px";
    s.style.left = (e.clientX - r.left - d / 2) + "px";
    s.style.top = (e.clientY - r.top - d / 2) + "px";
    b.appendChild(s);
    setTimeout(function () { s.remove(); }, 650);
  });

  /* ---------- Gallery tabs ---------- */
  var tabs = $$(".folder");
  var countEl = $(".gallery__count");
  function selectTab(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      var p = document.getElementById(t.getAttribute("aria-controls"));
      if (!p) return;
      p.hidden = !on;
      if (on) {
        p.classList.remove("is-entering");
        void p.offsetWidth;
        p.classList.add("is-entering");
        $$(".tile", p).forEach(function (el, i) { el.style.setProperty("--i", Math.min(i, 12)); });
        var sc = $(".gallery__scroll");
        if (sc) sc.scrollTop = 0;
      }
    });
    if (countEl) {
      var n = tab.querySelector("small");
      countEl.textContent = n ? n.textContent : "";
    }
    if (focus) tab.focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () {
      selectTab(t);
      if (window.innerWidth < 768) t.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "nearest", inline: "center" });
    });
    t.addEventListener("keydown", function (e) {
      var k = e.key, n = null;
      if (k === "ArrowRight" || k === "ArrowDown") n = tabs[(i + 1) % tabs.length];
      if (k === "ArrowLeft" || k === "ArrowUp") n = tabs[(i - 1 + tabs.length) % tabs.length];
      if (k === "Home") n = tabs[0];
      if (k === "End") n = tabs[tabs.length - 1];
      if (n) { e.preventDefault(); selectTab(n, true); }
    });
  });
  if (tabs[0]) selectTab(tabs[0]);

  $$(".more").forEach(function (b) {
    b.addEventListener("click", function () {
      var p = b.closest(".panel");
      p.classList.add("is-expanded");
      var first = $(".tile.is-extra", p);
      if (first) first.focus({ preventScroll: true });
    });
  });

  /* ---------- Lightbox ---------- */
  var lb = $(".lightbox");
  if (!lb) return;
  var stage = $(".lb__stage", lb);
  var cap = $(".lb__cap", lb);
  var cnt = $(".lb__count", lb);
  var strip = $(".lb__strip", lb);
  var ytLink = $(".lb__yt", lb);
  var blocked = {};
  function showFallback(it) {
    stage.innerHTML = '<div class="lb__fallback"><img alt="" src="https://i.ytimg.com/vi/' + it.yt + '/hqdefault.jpg"><div><p>' +
      (lb.getAttribute("data-noembed") || "") + '</p><a href="https://www.youtube.com/watch?v=' + it.yt + '" target="_blank" rel="noopener">' +
      '<svg class="icon" aria-hidden="true"><use href="#i-youtube"/></svg>' + (lb.getAttribute("data-watch") || "YouTube") + "</a></div></div>";
  }
  window.addEventListener("message", function (e) {
    if (!/youtube(-nocookie)?\.com$/.test(String(e.origin).replace(/^https?:\/\//, ""))) return;
    var d; try { d = typeof e.data === "string" ? JSON.parse(e.data) : e.data; } catch (x) { return; }
    if (!d || d.event !== "onError") return;
    var code = Number(d.info);
    var it = items[idx];
    if (it && it.yt && (code === 101 || code === 150 || code === 100 || code === 152 || code === 153)) {
      blocked[it.yt] = true;
      showFallback(it);
    }
  });
  var items = [], idx = 0, lastFocus = null;

  function itemsFrom(panel) {
    return $$(".tile", panel).map(function (t) {
      var img = $("img", t);
      var th = img ? img.getAttribute("src") : "";
      return t.hasAttribute("data-yt")
        ? { yt: t.getAttribute("data-yt"), cap: t.getAttribute("data-cap") || "", th: th }
        : { src: t.getAttribute("href"), cap: t.getAttribute("data-cap") || (img ? img.alt : ""), alt: img ? img.alt : "", th: th };
    });
  }
  function preload(i) {
    var it = items[(i + items.length) % items.length];
    if (it && it.src) { var im = new Image(); im.src = it.src; }
  }
  function render(dir) {
    var it = items[idx];
    stage.innerHTML = "";
    if (ytLink) {
      ytLink.hidden = !it.yt;
      if (it.yt) ytLink.href = "https://www.youtube.com/watch?v=" + it.yt;
    }
    if (it.yt) {
      if (blocked[it.yt]) { showFallback(it); }
      else {
        var f = document.createElement("iframe");
        var origin = /^https?:/.test(location.protocol) ? "&origin=" + encodeURIComponent(location.origin) : "";
        f.src = "https://www.youtube.com/embed/" + it.yt + "?autoplay=1&rel=0&playsinline=1&enablejsapi=1" + origin;
        f.title = it.cap || T.video;
        f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
        f.allowFullscreen = true;
        f.referrerPolicy = "strict-origin-when-cross-origin";
        f.addEventListener("load", function () {
          /* ask the player to report errors (embedding disabled = 101 / 150) */
          try { f.contentWindow.postMessage(JSON.stringify({ event: "listening", id: it.yt, channel: "widget" }), "*"); } catch (e) {}
        });
        stage.appendChild(f);
      }
    } else {
      var img = document.createElement("img");
      img.className = "is-loading";
      img.alt = it.alt || "";
      img.decoding = "async";
      img.onload = function () { requestAnimationFrame(function () { img.classList.remove("is-loading"); }); };
      img.src = it.src;
      if (dir && !reduce) img.style.transform = "translateX(" + (dir * 24) + "px)";
      stage.appendChild(img);
      requestAnimationFrame(function () { img.style.transform = ""; });
      preload(idx + 1); preload(idx - 1);
    }
    cap.textContent = it.cap || "";
    cnt.textContent = (idx + 1) + T.of + items.length;
    if (strip) {
      $$("button", strip).forEach(function (b, i) { b.setAttribute("aria-current", String(i === idx)); });
      var cur = strip.children[idx];
      if (cur) cur.scrollIntoView({ block: "nearest", inline: "center", behavior: reduce ? "auto" : "smooth" });
    }
  }
  function go(d) { idx = (idx + d + items.length) % items.length; render(d); }
  function open(panel, i) {
    items = itemsFrom(panel);
    if (!items.length) return;
    idx = i;
    lastFocus = document.activeElement;
    if (strip) {
      strip.innerHTML = "";
      items.forEach(function (it, n) {
        var b = document.createElement("button");
        b.type = "button";
        b.setAttribute("aria-label", (n + 1) + T.of + items.length);
        b.innerHTML = '<img alt="" loading="lazy" src="' + it.th + '">';
        b.addEventListener("click", function () { var d = n > idx ? 1 : -1; idx = n; render(d); });
        strip.appendChild(b);
      });
    }
    if (typeof lb.showModal === "function") lb.showModal(); else lb.setAttribute("open", "");
    doc.style.overflow = "hidden";
    render(0);
    requestAnimationFrame(function () { lb.classList.add("is-open"); });
    $(".lb__close", lb).focus();
  }
  function close() {
    lb.classList.remove("is-open");
    setTimeout(function () {
      stage.innerHTML = "";
      if (typeof lb.close === "function" && lb.open) lb.close(); else lb.removeAttribute("open");
      doc.style.overflow = "";
      if (lastFocus) lastFocus.focus({ preventScroll: true });
    }, reduce ? 0 : 200);
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest(".tile");
    if (!t) return;
    var panel = t.closest(".panel");
    if (!panel) return;
    e.preventDefault();
    open(panel, $$(".tile", panel).indexOf(t));
  });
  $$(".lb__prev", lb).forEach(function (b) { b.addEventListener("click", function (e) { e.stopPropagation(); go(-1); }); });
  $$(".lb__next", lb).forEach(function (b) { b.addEventListener("click", function (e) { e.stopPropagation(); go(1); }); });
  $(".lb__close", lb).addEventListener("click", close);
  lb.addEventListener("cancel", function (e) { e.preventDefault(); close(); });
  lb.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") go(1);
    else if (e.key === "ArrowLeft") go(-1);
  });
  stage.addEventListener("click", function (e) { if (e.target === stage) close(); });

  /* swipe */
  var sx = 0, sy = 0, tracking = false;
  stage.addEventListener("pointerdown", function (e) { if (e.pointerType === "mouse") return; tracking = true; sx = e.clientX; sy = e.clientY; });
  stage.addEventListener("pointerup", function (e) {
    if (!tracking) return;
    tracking = false;
    var dx = e.clientX - sx, dy = e.clientY - sy;
    if (Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy) * 1.4) go(dx < 0 ? 1 : -1);
    else if (dy > 90 && Math.abs(dy) > Math.abs(dx) * 1.4) close();
  });
  stage.addEventListener("pointercancel", function () { tracking = false; });
})();
