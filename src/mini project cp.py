<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BSRM — Mô hình hóa & Flow Logic</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#f9f8f5;--bg2:#f1f0ec;--bg3:#e8e7e2;--surface:#fff;
  --border:rgba(0,0,0,.09);--border2:rgba(0,0,0,.17);
  --text:#1a1a18;--text2:#5a5a55;--text3:#9a9a95;
  --blue:#378add;--blue-bg:#e6f1fb;--blue-text:#0c447c;--blue-bd:#85b7eb;
  --green:#1d9e75;--green-bg:#e1f5ee;--green-text:#085041;--green-bd:#5dcaa5;
  --amber:#ef9f27;--amber-bg:#faeeda;--amber-text:#633806;--amber-bd:#ef9f27;
  --purple:#6c5ce7;--purple-bg:#eeedfe;--purple-text:#3c3489;--purple-bd:#afa9ec;
  --coral:#e17055;--coral-bg:#faece7;--coral-text:#712b13;--coral-bd:#f0997b;
  --code-bg:#1a1a2e;
  --r:8px;--r-lg:12px;
}
@media(prefers-color-scheme:dark){:root{
  --bg:#1c1c1a;--bg2:#242422;--bg3:#2e2e2b;--surface:#2a2a28;
  --border:rgba(255,255,255,.09);--border2:rgba(255,255,255,.17);
  --text:#e8e7e2;--text2:#a0a09a;--text3:#6a6a65;
  --blue-bg:#042c53;--blue-text:#b5d4f4;--blue-bd:#185fa5;
  --green-bg:#04342c;--green-text:#9fe1cb;--green-bd:#0f6e56;
  --amber-bg:#412402;--amber-text:#fac775;--amber-bd:#854f0b;
  --purple-bg:#26215c;--purple-text:#cecbf6;--purple-bd:#534ab7;
  --coral-bg:#4a1b0c;--coral-text:#f5c4b3;--coral-bd:#993c1d;
}}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);min-height:100vh}

/* ── NAV ── */
nav{background:var(--surface);border-bottom:.5px solid var(--border2);padding:14px 32px;display:flex;align-items:center;gap:14px;position:sticky;top:0;z-index:100}
.nav-logo{width:34px;height:34px;border-radius:9px;background:var(--blue-bg);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.nav-title{font-size:15px;font-weight:600;color:var(--text)}
.nav-sub{font-size:12px;color:var(--text2);margin-top:1px}
.nav-tabs{margin-left:auto;display:flex;gap:4px}
.nav-tab{font-size:12px;font-weight:500;padding:6px 14px;border-radius:20px;border:.5px solid var(--border2);background:none;color:var(--text2);cursor:pointer;font-family:inherit;transition:all .15s}
.nav-tab:hover{background:var(--bg2);color:var(--text)}
.nav-tab.active{background:var(--text);color:var(--bg);border-color:var(--text)}
.btn-goto{font-size:12px;font-weight:500;padding:6px 14px;border-radius:20px;background:var(--green-bg);color:var(--green-text);border:.5px solid var(--green-bd);cursor:pointer;font-family:inherit;text-decoration:none;display:inline-flex;align-items:center;gap:5px;margin-left:8px}
.btn-goto:hover{filter:brightness(.95)}

/* ── PAGE TABS ── */
.page{display:none}.page.active{display:block}

/* ── HERO ── */
.hero{text-align:center;padding:48px 24px 32px;max-width:680px;margin:0 auto}
.hero-badge{display:inline-block;font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;background:var(--blue-bg);color:var(--blue-text);border:.5px solid var(--blue-bd);margin-bottom:16px}
.hero h1{font-size:28px;font-weight:700;line-height:1.3;margin-bottom:10px}
.hero p{font-size:15px;color:var(--text2);line-height:1.7}

/* ── PROBLEM CARDS ── */
.cards{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;max-width:900px;margin:0 auto 40px;padding:0 24px}
.card{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:18px 20px}
.card-icon{font-size:22px;margin-bottom:10px}
.card-title{font-size:13px;font-weight:600;margin-bottom:6px}
.card-body{font-size:13px;color:var(--text2);line-height:1.65}
.ck{display:inline-block;font-family:'SFMono-Regular',Consolas,monospace;font-size:11.5px;background:var(--bg2);border:.5px solid var(--border2);border-radius:4px;padding:1px 6px;color:var(--blue-text)}
.ck-g{color:var(--green-text);background:var(--green-bg);border-color:var(--green-bd)}
.ck-a{color:var(--amber-text);background:var(--amber-bg);border-color:var(--amber-bd)}
.ck-p{color:var(--purple-text);background:var(--purple-bg);border-color:var(--purple-bd)}
.ck-c{color:var(--coral-text);background:var(--coral-bg);border-color:var(--coral-bd)}

/* ── SECTION HEADER ── */
.sec-wrap{max-width:900px;margin:0 auto;padding:0 24px 48px}
.sec-hdr{display:flex;align-items:center;gap:10px;margin-bottom:20px}
.sec-badge{font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px}
.sec-hdr h2{font-size:18px;font-weight:600}
.divider{border:none;border-top:.5px solid var(--border);margin:32px 0}

/* ══ FLOW DIAGRAM ══ */
.flow-wrap{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:28px 24px;overflow-x:auto}
.flow{display:flex;flex-direction:column;align-items:center;gap:0}
.flow-row{display:flex;align-items:center;gap:0;width:100%;justify-content:center}
.flow-arrow-v{width:2px;height:24px;background:var(--border2);margin:0 auto}
.flow-arrow-h{width:28px;height:2px;background:var(--border2);flex-shrink:0}
.flow-node{
  border:.5px solid var(--border2);border-radius:var(--r);padding:13px 18px;
  font-size:13px;cursor:pointer;transition:all .15s;text-align:center;
  background:var(--bg2);min-width:140px;user-select:none;position:relative;
}
.flow-node:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.1)}
.flow-node.active-node{box-shadow:0 0 0 2px var(--blue)}
.flow-node .fn-icon{font-size:18px;margin-bottom:5px}
.flow-node .fn-title{font-weight:600;font-size:12.5px;margin-bottom:2px}
.flow-node .fn-sub{font-size:11px;color:var(--text2)}
.fn-blue  {border-color:var(--blue-bd)!important;background:var(--blue-bg)!important}
.fn-green {border-color:var(--green-bd)!important;background:var(--green-bg)!important}
.fn-amber {border-color:var(--amber-bd)!important;background:var(--amber-bg)!important}
.fn-purple{border-color:var(--purple-bd)!important;background:var(--purple-bg)!important}
.fn-coral {border-color:var(--coral-bd)!important;background:var(--coral-bg)!important}
.fn-gray  {border-color:var(--border2)!important;background:var(--bg2)!important}
.fn-blue  .fn-title{color:var(--blue-text)}
.fn-green .fn-title{color:var(--green-text)}
.fn-amber .fn-title{color:var(--amber-text)}
.fn-purple .fn-title{color:var(--purple-text)}
.fn-coral .fn-title{color:var(--coral-text)}

.flow-branch{display:flex;align-items:flex-start;gap:0;width:100%;justify-content:center;margin:0}
.branch-line{width:.5px;background:var(--border2);align-self:stretch;margin-top:0}

/* node detail panel */
.node-detail{
  background:var(--bg2);border:.5px solid var(--border2);border-radius:var(--r-lg);
  padding:18px 20px;margin-top:20px;font-size:13.5px;line-height:1.75;
  transition:all .2s;
}
.node-detail h3{font-size:15px;font-weight:600;margin-bottom:8px}
.nd-why{border-left:3px solid var(--blue);background:color-mix(in srgb,var(--blue-bg) 30%,transparent);border-radius:0 var(--r) var(--r) 0;padding:10px 14px;margin:10px 0;font-size:13px;line-height:1.7}
.nd-ex {border-left:3px solid var(--green);background:color-mix(in srgb,var(--green-bg) 30%,transparent);border-radius:0 var(--r) var(--r) 0;padding:10px 14px;margin:10px 0;font-size:13px;line-height:1.7}
.nd-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.nd-lbl-b{color:var(--blue-text)}.nd-lbl-g{color:var(--green-text)}

/* ══ VARIABLE MAP ══ */
.var-map{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px}
.var-card{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:16px 18px}
.vc-head{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.vc-badge{font-size:18px}
.vc-name{font-size:14px;font-weight:700}
.vc-type{font-size:11px;color:var(--text2);margin-top:1px}
.vc-body{font-size:13px;color:var(--text2);line-height:1.65}
.vc-body strong{color:var(--text);font-weight:600}
.vc-ex{font-family:'SFMono-Regular',Consolas,monospace;font-size:12px;background:var(--bg2);border-radius:6px;padding:8px 10px;margin-top:8px;color:var(--text);line-height:1.7;border:.5px solid var(--border2)}
.flow-arrow-down{display:flex;flex-direction:column;align-items:center;margin:6px 0}
.flow-arrow-down span{font-size:11px;color:var(--text3);margin-top:2px}

/* ══ CONSTRAINT TABLE ══ */
.ct-table{width:100%;border-collapse:collapse;font-size:13px}
.ct-table th{text-align:left;padding:9px 12px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text3);border-bottom:.5px solid var(--border2);background:var(--bg2)}
.ct-table td{padding:11px 12px;border-bottom:.5px solid var(--border);vertical-align:top;line-height:1.65}
.ct-table tr:last-child td{border-bottom:none}
.ct-table td:first-child{font-family:'SFMono-Regular',Consolas,monospace;font-size:12px;white-space:nowrap;color:var(--blue-text);width:28%}
.ct-badge{display:inline-block;font-size:10px;font-weight:600;padding:2px 7px;border-radius:10px;margin-right:5px}

/* ══ ANIMATION PAGE ══ */
.anim-layout{display:grid;grid-template-columns:340px 1fr;gap:20px;max-width:1000px;margin:0 auto;padding:0 24px 48px}

/* graph canvas */
.graph-panel{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:0;overflow:hidden;position:relative}
.graph-panel canvas{display:block;width:100%;height:320px}
.graph-legend{padding:12px 16px;border-top:.5px solid var(--border);display:flex;gap:14px;flex-wrap:wrap}
.gl-item{display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--text2)}
.gl-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}

/* step panel */
.step-panel{display:flex;flex-direction:column;gap:12px}
.step-counter{font-size:12px;color:var(--text2);font-weight:500}
.step-title-big{font-size:17px;font-weight:600;margin-bottom:4px}
.step-desc{font-size:13.5px;color:var(--text2);line-height:1.75;margin-bottom:8px}

/* state table */
.state-box{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);overflow:hidden}
.state-hdr{padding:9px 14px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text2);border-bottom:.5px solid var(--border);background:var(--bg2)}
.state-body{padding:12px 14px}
.state-row{display:grid;grid-template-columns:auto 1fr;gap:6px 10px;align-items:start;margin-bottom:6px;font-size:13px;line-height:1.6}
.state-row:last-child{margin-bottom:0}
.state-key{font-family:'SFMono-Regular',Consolas,monospace;font-size:11.5px;color:var(--blue-text);white-space:nowrap}
.state-val{color:var(--text)}
.state-val .hi{color:var(--green-text);font-weight:600}
.state-val .lo{color:var(--amber-text)}

/* constraint highlight box */
.c-box{border-radius:var(--r);padding:10px 14px;font-size:13px;line-height:1.7;font-family:'SFMono-Regular',Consolas,monospace;border:.5px solid var(--border2);background:var(--bg2)}
.c-box .active-c{background:color-mix(in srgb,var(--green-bg) 60%,transparent);border-radius:4px;padding:1px 4px;color:var(--green-text);font-weight:600}

/* nav buttons */
.anim-controls{display:flex;align-items:center;gap:10px;margin-top:4px}
.ctrl-btn{font-size:13px;font-weight:500;padding:8px 18px;border-radius:8px;border:.5px solid var(--border2);background:var(--bg2);color:var(--text);cursor:pointer;font-family:inherit;transition:all .12s}
.ctrl-btn:hover:not(:disabled){background:var(--bg3)}
.ctrl-btn:disabled{opacity:.35;cursor:default}
.ctrl-btn.primary{background:var(--text);color:var(--bg);border-color:var(--text)}
.ctrl-btn.primary:hover:not(:disabled){opacity:.85}
.step-prog{flex:1;height:4px;background:var(--bg3);border-radius:2px;overflow:hidden}
.step-prog-fill{height:100%;background:var(--blue);border-radius:2px;transition:width .3s}

/* result badge */
.result-badge{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;padding:5px 12px;border-radius:20px;background:var(--green-bg);color:var(--green-text);border:.5px solid var(--green-bd)}

@media(max-width:720px){
  .cards{grid-template-columns:1fr}
  .var-map{grid-template-columns:1fr}
  .anim-layout{grid-template-columns:1fr}
  nav{padding:12px 16px}.nav-tabs{display:none}
}
</style>
</head>
<body>

<!-- ── NAV ── -->
<nav>
  <div class="nav-logo">🛠</div>
  <div>
    <div class="nav-title">BSRM CP-SAT</div>
    <div class="nav-sub">Balanced Staff Routing · N khách hàng · K kỹ thuật viên</div>
  </div>
  <div class="nav-tabs">
    <button class="nav-tab active" onclick="switchPage('overview',this)">📐 Mô hình hóa</button>
    <button class="nav-tab" onclick="switchPage('anim',this)">▶ Animation N=3 K=2</button>
  </div>
  <a class="btn-goto" href="bsrm_explainer.html">Code chi tiết →</a>
</nav>

<!-- ══════════════════════════════════════════════════════
     PAGE 1: OVERVIEW / MODEL
══════════════════════════════════════════════════════ -->
<div class="page active" id="page-overview">

<div class="hero">
  <div class="hero-badge">Constraint Programming · OR-Tools CP-SAT</div>
  <h1>Logic giải bài toán<br>Balanced Staff Routing</h1>
  <p>Bài toán: Phân công N khách hàng cho K kỹ thuật viên xuất phát từ depot, sao cho thời gian làm việc của người bận nhất là nhỏ nhất (Minimax Makespan).</p>
</div>

<!-- Problem cards -->
<div class="cards">
  <div class="card">
    <div class="card-icon">📥</div>
    <div class="card-title">Đầu vào</div>
    <div class="card-body">
      <span class="ck">N</span> khách hàng, <span class="ck">K</span> kỹ thuật viên<br>
      <span class="ck">d[j]</span> — thời gian phục vụ tại KH j<br>
      <span class="ck">matrix[i][j]</span> — thời gian di chuyển từ i đến j<br>
      Node <span class="ck">0</span> = depot (điểm xuất phát)
    </div>
  </div>
  <div class="card">
    <div class="card-icon">🎯</div>
    <div class="card-title">Mục tiêu</div>
    <div class="card-body">
      Minimize <span class="ck-c">z = max(y[1], y[2], ..., y[K])</span><br><br>
      Trong đó <span class="ck-g">y[k]</span> = tổng thời gian di chuyển + phục vụ của KTV k<br><br>
      → Cân bằng tải giữa các KTV
    </div>
  </div>
  <div class="card">
    <div class="card-icon">📤</div>
    <div class="card-title">Đầu ra</div>
    <div class="card-body">
      K tuyến đường, mỗi tuyến có dạng<br>
      <span class="ck">0 → j₁ → j₂ → ... → 0</span><br><br>
      Mỗi KH xuất hiện đúng 1 lần trong toàn bộ K tuyến
    </div>
  </div>
</div>

<!-- FLOW DIAGRAM -->
<div class="sec-wrap">
  <div class="sec-hdr">
    <span class="sec-badge badge-blue" style="background:var(--blue-bg);color:var(--blue-text);border:.5px solid var(--blue-bd)">Flow tổng quan</span>
    <h2>Logic mô hình CP-SAT — click vào bước để xem chi tiết</h2>
  </div>

  <div class="flow-wrap">
    <div class="flow">

      <!-- Row 1: Input -->
      <div class="flow-row">
        <div class="flow-node fn-gray" onclick="showNode('n-input')">
          <div class="fn-icon">📥</div>
          <div class="fn-title">Đọc đầu vào</div>
          <div class="fn-sub">N, K, d[], matrix[][]</div>
        </div>
      </div>
      <div class="flow-arrow-v"></div>

      <!-- Row 2: Declare vars -->
      <div class="flow-row">
        <div class="flow-node fn-blue" onclick="showNode('n-vars')">
          <div class="fn-icon">🔢</div>
          <div class="fn-title">Khai báo biến</div>
          <div class="fn-sub">x[i,j,k] · y[k] · z · self_loop</div>
        </div>
      </div>
      <div class="flow-arrow-v"></div>

      <!-- Row 3: 3 constraints side by side -->
      <div class="flow-row" style="gap:0">
        <!-- left branch line -->
        <div style="display:flex;flex-direction:column;align-items:flex-end;width:160px">
          <div style="width:80px;height:.5px;background:var(--border2);margin-top:0;align-self:flex-end"></div>
          <div style="width:.5px;height:24px;background:var(--border2);align-self:flex-end"></div>
        </div>
        <!-- center node: RB1 -->
        <div style="display:flex;flex-direction:column;align-items:center">
          <div class="flow-node fn-purple" onclick="showNode('n-c1')" style="min-width:160px">
            <div class="fn-icon">✅</div>
            <div class="fn-title">Ràng buộc 1</div>
            <div class="fn-sub">Mỗi KH phục vụ đúng 1 lần</div>
          </div>
        </div>
        <!-- right branch line -->
        <div style="display:flex;flex-direction:column;align-items:flex-start;width:160px">
          <div style="width:80px;height:.5px;background:var(--border2);margin-top:0"></div>
          <div style="width:.5px;height:24px;background:var(--border2)"></div>
        </div>
      </div>

      <!-- Branch: RB2 and RB3 side by side -->
      <div class="flow-row" style="gap:20px;align-items:flex-start">
        <div class="flow-node fn-purple" onclick="showNode('n-c2')" style="min-width:160px">
          <div class="fn-icon">🔄</div>
          <div class="fn-title">Ràng buộc 2</div>
          <div class="fn-sub">Bảo toàn luồng / KTV</div>
        </div>
        <div style="width:20px"></div>
        <div class="flow-node fn-amber" onclick="showNode('n-circuit')" style="min-width:160px">
          <div class="fn-icon">⭕</div>
          <div class="fn-title">Ràng buộc 3</div>
          <div class="fn-sub">AddCircuit — chống subtour</div>
        </div>
      </div>
      <div class="flow-arrow-v"></div>

      <!-- Row: Workload -->
      <div class="flow-row">
        <div class="flow-node fn-green" onclick="showNode('n-workload')">
          <div class="fn-icon">⏱</div>
          <div class="fn-title">Tính Workload y[k]</div>
          <div class="fn-sub">∑ x[i,j,k]×(travel+service)</div>
        </div>
      </div>
      <div class="flow-arrow-v"></div>

      <!-- Row: Objective -->
      <div class="flow-row">
        <div class="flow-node fn-coral" onclick="showNode('n-obj')">
          <div class="fn-icon">🎯</div>
          <div class="fn-title">Hàm mục tiêu</div>
          <div class="fn-sub">Minimize z = max(y[k])</div>
        </div>
      </div>
      <div class="flow-arrow-v"></div>

      <!-- Row: Solve -->
      <div class="flow-row" style="gap:20px">
        <div class="flow-node fn-blue" onclick="showNode('n-solve')" style="min-width:130px">
          <div class="fn-icon">🔍</div>
          <div class="fn-title">CP-SAT Solver</div>
          <div class="fn-sub">Branch & Bound + Propagation</div>
        </div>
        <div style="display:flex;align-items:center;gap:0">
          <div style="width:24px;height:.5px;background:var(--border2)"></div>
          <div class="flow-node fn-green" onclick="showNode('n-output')" style="min-width:130px">
            <div class="fn-icon">📤</div>
            <div class="fn-title">Truy vết & xuất</div>
            <div class="fn-sub">route[k] = 0→j₁→...→0</div>
          </div>
        </div>
      </div>

    </div><!-- .flow -->
  </div><!-- .flow-wrap -->

  <!-- Node detail panel (hidden by default) -->
  <div class="node-detail" id="node-detail" style="display:none"></div>

  <hr>

  <!-- VARIABLE MAP -->
  <div class="sec-hdr" style="margin-top:32px">
    <span class="sec-badge" style="background:var(--purple-bg);color:var(--purple-text);border:.5px solid var(--purple-bd)">Biến quyết định</span>
    <h2>Bản đồ biến — cái gì điều khiển cái gì?</h2>
  </div>

  <div class="var-map">
    <div class="var-card">
      <div class="vc-head">
        <div class="vc-badge">🔵</div>
        <div><div class="vc-name"><span class="ck">x[i, j, k]</span></div><div class="vc-type">BoolVar — biến quyết định cốt lõi</div></div>
      </div>
      <div class="vc-body">
        <strong>Ý nghĩa:</strong> = 1 nếu KTV k đi từ điểm i sang điểm j, = 0 nếu không.<br>
        Đây là "bộ khung xương" của toàn bộ mô hình — mọi ràng buộc và hàm mục tiêu đều phụ thuộc vào x.
        <div class="vc-ex">x[0,1,1] = 1  → KTV 1 đi depot→KH1<br>x[1,3,1] = 1  → KTV 1 đi KH1→KH3<br>x[3,0,1] = 1  → KTV 1 quay về depot</div>
      </div>
    </div>
    <div class="var-card">
      <div class="vc-head">
        <div class="vc-badge">🟡</div>
        <div><div class="vc-name"><span class="ck">self_loop[i, k]</span></div><div class="vc-type">BoolVar — biến phụ trợ cho AddCircuit</div></div>
      </div>
      <div class="vc-body">
        <strong>Ý nghĩa:</strong> = 1 khi KTV k <em>không</em> ghé KH i (i do KTV khác phục vụ).<br>
        Cần thiết để AddCircuit hoạt động đúng — mỗi node phải có đúng 1 "cạnh vào" kể cả khi KTV bỏ qua node đó.
        <div class="vc-ex">self_loop[2,1] = 1 → KTV 1 bỏ qua KH2<br>self_loop[2,2] = 0 → KTV 2 có ghé KH2</div>
      </div>
    </div>
    <div class="var-card">
      <div class="vc-head">
        <div class="vc-badge">🟢</div>
        <div><div class="vc-name"><span class="ck">y[k]</span></div><div class="vc-type">IntVar — workload của KTV k</div></div>
      </div>
      <div class="vc-body">
        <strong>Ý nghĩa:</strong> Tổng thời gian làm việc của KTV k = tổng (di chuyển + phục vụ) trên toàn tuyến.<br>
        Được xác định bởi ràng buộc: y[k] = ∑ x[i,j,k]·(matrix[i][j] + d[j])
        <div class="vc-ex">Nếu KTV 1 đi 0→1→3→0:<br>y[1] = (10+5)+(18+6)+(20+0) = 59 phút</div>
      </div>
    </div>
    <div class="var-card">
      <div class="vc-head">
        <div class="vc-badge">🔴</div>
        <div><div class="vc-name"><span class="ck">z</span></div><div class="vc-type">IntVar — mục tiêu tối thiểu hóa</div></div>
      </div>
      <div class="vc-body">
        <strong>Ý nghĩa:</strong> Workload của KTV bận nhất. Ràng buộc z ≥ y[k] với mọi k buộc z phải ≥ max(y[k]).<br>
        Minimize(z) → solver tìm phân công công bằng nhất có thể.
        <div class="vc-ex">y[1]=59, y[2]=38 → z = 59<br>Solver thử tìm phân công tốt hơn...</div>
      </div>
    </div>
  </div>

  <!-- arrows showing dependency -->
  <div style="background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:16px 20px;font-size:13.5px;line-height:1.9;color:var(--text2)">
    <strong style="color:var(--text);display:block;margin-bottom:8px">Chuỗi phụ thuộc logic:</strong>
    <span class="ck">x[i,j,k]</span> được solver chọn (0 hoặc 1)
    &nbsp;→&nbsp; các x này xác định <span class="ck-g">y[k]</span> qua ràng buộc workload
    &nbsp;→&nbsp; <span class="ck-c">z</span> = max của tất cả y[k]
    &nbsp;→&nbsp; solver minimize z
    &nbsp;→&nbsp; buộc phải tìm x tốt hơn
    &nbsp;→&nbsp; vòng lặp B&amp;B tiếp tục cho đến khi z tối ưu
  </div>

  <hr>

  <!-- CONSTRAINT TABLE -->
  <div class="sec-hdr" style="margin-top:32px">
    <span class="sec-badge" style="background:var(--amber-bg);color:var(--amber-text);border:.5px solid var(--amber-bd)">Ràng buộc</span>
    <h2>Bảng tổng hợp 5 ràng buộc</h2>
  </div>

  <div style="background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);overflow:hidden">
    <table class="ct-table">
      <thead>
        <tr>
          <th>Công thức</th>
          <th>Tên & Ý nghĩa</th>
          <th>Nếu vi phạm...</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>∑<sub>k,i</sub> x[i,j,k] = 1<br><span style="font-size:10px;color:var(--text3)">với mọi j ∈ 1..N</span></td>
          <td><span class="ct-badge" style="background:var(--purple-bg);color:var(--purple-text)">RB1</span><strong>Phục vụ đúng 1 lần</strong><br><span style="color:var(--text2)">Mỗi KH phải có đúng 1 cạnh đi vào, từ bất kỳ KTV nào</span></td>
          <td style="color:var(--amber-text)">KH bị bỏ sót hoặc phục vụ 2 lần</td>
        </tr>
        <tr>
          <td>∑<sub>i</sub> x[i,j,k] + sl[j,k] = 1<br><span style="font-size:10px;color:var(--text3)">với mọi j,k</span></td>
          <td><span class="ct-badge" style="background:var(--purple-bg);color:var(--purple-text)">RB2</span><strong>Bảo toàn luồng / KTV</strong><br><span style="color:var(--text2)">Mỗi KTV: với mỗi KH, hoặc đến hoặc bỏ qua (self_loop)</span></td>
          <td style="color:var(--amber-text)">AddCircuit lỗi — node thiếu cạnh vào</td>
        </tr>
        <tr>
          <td>AddCircuit(arcs<sub>k</sub>)<br><span style="font-size:10px;color:var(--text3)">với mọi k</span></td>
          <td><span class="ct-badge" style="background:var(--amber-bg);color:var(--amber-text)">RB3</span><strong>Tuyến hợp lệ</strong><br><span style="color:var(--text2)">Mọi cạnh được chọn tạo thành đúng 1 chu trình Hamiltonian</span></td>
          <td style="color:var(--amber-text)">Subtour — vòng nhỏ không qua depot</td>
        </tr>
        <tr>
          <td>y[k] = ∑<sub>i,j</sub> x[i,j,k]·(m[i][j]+d[j])<br><span style="font-size:10px;color:var(--text3)">với mọi k</span></td>
          <td><span class="ct-badge" style="background:var(--green-bg);color:var(--green-text)">RB4</span><strong>Định nghĩa workload</strong><br><span style="color:var(--text2)">y[k] được liên kết với x qua tổng chi phí cạnh được chọn</span></td>
          <td style="color:var(--amber-text)">y[k] không phản ánh đúng thực tế tuyến đường</td>
        </tr>
        <tr>
          <td>z ≥ y[k]<br><span style="font-size:10px;color:var(--text3)">với mọi k</span></td>
          <td><span class="ct-badge" style="background:var(--coral-bg);color:var(--coral-text)">RB5</span><strong>Định nghĩa minimax</strong><br><span style="color:var(--text2)">z ép phải ≥ max(y[k]) — kết hợp Minimize(z) = tối thiểu max</span></td>
          <td style="color:var(--amber-text)">z không phản ánh KTV bận nhất</td>
        </tr>
      </tbody>
    </table>
  </div>

</div><!-- .sec-wrap -->
</div><!-- #page-overview -->


<!-- ══════════════════════════════════════════════════════
     PAGE 2: ANIMATION
══════════════════════════════════════════════════════ -->
<div class="page" id="page-anim">

<div class="hero" style="padding-bottom:20px">
  <div class="hero-badge">Ví dụ số — N=3, K=2</div>
  <h1>Solver hoạt động như thế nào?</h1>
  <p>Theo dõi từng bước: từ bài toán đầu vào → khai báo biến → áp ràng buộc → tìm nghiệm → xuất tuyến đường.</p>
</div>

<div class="anim-layout">

  <!-- LEFT: Graph -->
  <div>
    <div class="graph-panel">
      <canvas id="graphCanvas" width="680" height="640"></canvas>
      <div class="graph-legend">
        <div class="gl-item"><div class="gl-dot" style="background:#378add"></div>Depot (0)</div>
        <div class="gl-item"><div class="gl-dot" style="background:#1d9e75"></div>Khách hàng</div>
        <div class="gl-item"><div class="gl-dot" style="background:#ef9f27;width:10px;height:3px;border-radius:2px"></div>KTV 1</div>
        <div class="gl-item"><div class="gl-dot" style="background:#6c5ce7;width:10px;height:3px;border-radius:2px"></div>KTV 2</div>
      </div>
    </div>
  </div>

  <!-- RIGHT: Step explanation -->
  <div class="step-panel">
    <div style="display:flex;align-items:center;gap:10px">
      <span class="step-counter" id="stepCounter">Bước 1 / 9</span>
      <div class="step-prog"><div class="step-prog-fill" id="stepProg" style="width:11%"></div></div>
    </div>

    <div>
      <div class="step-title-big" id="stepTitle">Bài toán đầu vào</div>
      <div class="step-desc" id="stepDesc">Đọc dữ liệu đầu vào: N=3 khách hàng, K=2 kỹ thuật viên. Đồ thị có 4 node (0=depot, 1,2,3=khách hàng) với ma trận khoảng cách và thời gian phục vụ.</div>
    </div>

    <div class="state-box">
      <div class="state-hdr" id="stateHdr">Trạng thái dữ liệu</div>
      <div class="state-body" id="stateBody">
        <div class="state-row"><span class="state-key">N, K</span><span class="state-val">3 khách hàng, 2 kỹ thuật viên</span></div>
        <div class="state-row"><span class="state-key">d[]</span><span class="state-val">[0, 5, 8, 6] phút</span></div>
        <div class="state-row"><span class="state-key">matrix[0]</span><span class="state-val">[0, 10, 15, 20]</span></div>
        <div class="state-row"><span class="state-key">matrix[1]</span><span class="state-val">[10, 0, 12, 18]</span></div>
        <div class="state-row"><span class="state-key">matrix[2]</span><span class="state-val">[15, 12, 0, 14]</span></div>
        <div class="state-row"><span class="state-key">matrix[3]</span><span class="state-val">[20, 18, 14, 0]</span></div>
      </div>
    </div>

    <div class="state-box" id="constraintBox" style="display:none">
      <div class="state-hdr">Ràng buộc đang áp dụng</div>
      <div class="state-body"><div class="c-box" id="constraintCode"></div></div>
    </div>

    <div class="anim-controls">
      <button class="ctrl-btn" id="btnPrev" onclick="stepAnim(-1)" disabled>← Trước</button>
      <button class="ctrl-btn primary" id="btnNext" onclick="stepAnim(1)">Tiếp theo →</button>
    </div>

    <div id="resultBadge" style="display:none">
      <div class="result-badge">✓ Nghiệm tối ưu — z = 59 phút</div>
    </div>
  </div>

</div>
</div><!-- #page-anim -->


<script>
/* ═══════════════════════════════════════════
   PAGE SWITCHING
═══════════════════════════════════════════ */
function switchPage(id, btn) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
  document.getElementById('page-' + id).classList.add('active');
  if (btn) btn.classList.add('active');
  if (id === 'anim') { requestAnimationFrame(drawGraph); }
}

/* ═══════════════════════════════════════════
   FLOW NODE DETAIL
═══════════════════════════════════════════ */
const nodeData = {
  'n-input': {
    title: '📥 Đọc đầu vào',
    html: `<p>Đọc N, K, mảng <span class="ck">d[]</span> và ma trận <span class="ck">matrix[][]</span>. Thêm <span class="ck-g">d[0] = 0</span> (depot không có thời gian phục vụ) để mọi index thống nhất từ 0..N trong suốt mô hình.</p>
    <div class="nd-ex"><div class="nd-lbl nd-lbl-g">Ví dụ N=3, K=2</div>d = [<b>0</b>, 5, 8, 6] — chỉ số 0 là depot<br>matrix[0][1] = 10 phút (depot→KH1)<br>matrix[1][3] = 18 phút (KH1→KH3)</div>`
  },
  'n-vars': {
    title: '🔢 Khai báo biến',
    html: `<p>Tạo tất cả biến quyết định trước khi viết ràng buộc — đây là quy tắc bắt buộc của CP-SAT (lập trình khai báo). 4 loại biến: <span class="ck">x</span> (cạnh nào được đi), <span class="ck">y[k]</span> (workload), <span class="ck">self_loop</span> (KTV bỏ qua node nào), <span class="ck">z</span> (mục tiêu).</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Tại sao khai báo UB?</div>CP-SAT yêu cầu mọi IntVar phải có domain giới hạn [lo, hi]. UB = N × max_travel + sum(d) là giới hạn trên tệ nhất: 1 KTV đi hết N cạnh xa nhất + phục vụ mọi KH.</div>`
  },
  'n-c1': {
    title: '✅ Ràng buộc 1 — Phục vụ đúng 1 lần',
    html: `<p>Với mỗi KH j: <span class="ck">∑<sub>k,i</sub> x[i,j,k] = 1</span>. Tổng số cạnh đi vào j (gộp tất cả KTV và điểm xuất phát) phải bằng đúng 1.</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Tại sao == 1 chứ không phải >= 1?</div>≥1 cho phép 2 KTV cùng ghé 1 KH. =1 ép chính xác 1 KTV phục vụ 1 KH, tránh trùng lặp lãng phí.</div>
    <div class="nd-ex"><div class="nd-lbl nd-lbl-g">Với j=2, N=3, K=2:</div>x[0,2,1]+x[1,2,1]+x[3,2,1]+x[0,2,2]+x[1,2,2]+x[3,2,2] = 1<br>→ Đúng 1 trong 6 cạnh được chọn</div>`
  },
  'n-c2': {
    title: '🔄 Ràng buộc 2 — Bảo toàn luồng / KTV',
    html: `<p>Với mỗi cặp (j,k): <span class="ck">∑<sub>i</sub> x[i,j,k] + self_loop[j,k] = 1</span>. Xét từng KTV riêng lẻ: hoặc KTV k đến j (sum=1, self_loop=0), hoặc KTV k bỏ qua j (sum=0, self_loop=1).</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Self_loop là gì?</div>AddCircuit yêu cầu mọi node có đúng 1 cạnh vào trong đồ thị của KTV k. Nếu KTV k không ghé j, ta cần "cạnh ảo" j→j (self_loop) để AddCircuit không bị lỗi.</div>`
  },
  'n-circuit': {
    title: '⭕ Ràng buộc 3 — AddCircuit',
    html: `<p>Với mỗi KTV k: <span class="ck">model.AddCircuit(arcs)</span>. Các cạnh được chọn (x=1 hoặc self_loop=1) phải tạo thành đúng 1 chu trình Hamiltonian duy nhất qua tất cả node.</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Tại sao cần AddCircuit thay vì chỉ flow?</div>Flow thông thường cho phép subtour: KTV 1 đi vòng 1→2→1 không qua depot — node 1,2 đều có 1 cạnh vào/ra nhưng tuyến sai hoàn toàn. AddCircuit loại trừ điều này bằng cách yêu cầu tất cả tạo 1 vòng duy nhất.</div>
    <div class="nd-ex"><div class="nd-lbl nd-lbl-g">KTV 1, tuyến 0→1→3→0:</div>Cạnh bật: (0,1,x[0,1,1]=1), (1,3,x[1,3,1]=1), (3,0,x[3,0,1]=1), (2,2,sl[2,1]=1)<br>→ Chu trình hợp lệ ✓</div>`
  },
  'n-workload': {
    title: '⏱ Tính Workload y[k]',
    html: `<p><span class="ck">y[k] = ∑ x[i,j,k] × (matrix[i][j] + d[j])</span>. Mỗi cạnh được đi (x=1) đóng góp thời gian di chuyển + thời gian phục vụ tại điểm đến. Cạnh không được đi (x=0) đóng góp 0.</p>
    <div class="nd-ex"><div class="nd-lbl nd-lbl-g">KTV 1 đi 0→1→3→0:</div>0→1: (10+5)=15 · 1→3: (18+6)=24 · 3→0: (20+0)=20<br>y[1] = 15+24+20 = <b>59 phút</b></div>`
  },
  'n-obj': {
    title: '🎯 Hàm mục tiêu Minimax',
    html: `<p>Thêm K ràng buộc <span class="ck">z ≥ y[k]</span> với mọi k, rồi <span class="ck">model.Minimize(z)</span>. Vì z phải ≥ tất cả y[k], solver buộc phải tìm phân công mà KTV bận nhất làm ít nhất.</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Min-max vs Min-sum</div>Min-sum tối thiểu tổng thời gian — có thể 1 người làm 80 phút, 1 người làm 0. Min-max tối thiểu thời gian của người bận nhất — phân công công bằng hơn.</div>`
  },
  'n-solve': {
    title: '🔍 CP-SAT Solver — Branch & Bound',
    html: `<p>Solver thử các lời giải bằng Branch & Bound kết hợp Constraint Propagation. Mỗi lần tìm được nghiệm tốt hơn, cập nhật upper bound của z và tiếp tục tìm. Dừng khi chứng minh được không còn nghiệm tốt hơn.</p>
    <div class="nd-why"><div class="nd-lbl nd-lbl-b">Max 100 giây</div>Nếu hết thời gian, trả về nghiệm FEASIBLE (hợp lệ nhưng chưa chứng minh tối ưu). Vẫn in được kết quả, chỉ không chắc là tốt nhất.</div>`
  },
  'n-output': {
    title: '📤 Truy vết & xuất tuyến đường',
    html: `<p>Sau khi có nghiệm, truy vết route của từng KTV bằng cách đọc giá trị <span class="ck">solver.Value(x[current,j,k])</span>. Bắt đầu từ depot (0), theo từng cạnh được chọn cho đến khi quay về depot.</p>
    <div class="nd-ex"><div class="nd-lbl nd-lbl-g">Truy vết KTV 1:</div>current=0 → x[0,1,1]=1 → current=1<br>current=1 → x[1,3,1]=1 → current=3<br>current=3 → x[3,0,1]=1 → current=0 → dừng<br>route = [0,1,3,0], len=4</div>`
  }
};

function showNode(id) {
  const d = nodeData[id];
  if (!d) return;
  const panel = document.getElementById('node-detail');
  panel.style.display = 'block';
  panel.innerHTML = `<h3>${d.title}</h3>${d.html}`;
  panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  document.querySelectorAll('.flow-node').forEach(n => n.classList.remove('active-node'));
  // highlight clicked
  event.currentTarget.classList.add('active-node');
}

/* ═══════════════════════════════════════════
   CANVAS GRAPH
═══════════════════════════════════════════ */
const NODES = [
  { id:0, label:'0\n(Depot)', x:170, y:160, color:'#378add' },
  { id:1, label:'1\n(KH1)',   x:80,  y:290, color:'#1d9e75' },
  { id:2, label:'2\n(KH2)',   x:260, y:290, color:'#1d9e75' },
  { id:3, label:'3\n(KH3)',   x:170, y:400, color:'#1d9e75' },
];
const MATRIX = [
  [0,10,15,20],[10,0,12,18],[15,12,0,14],[20,18,14,0]
];
const D = [0,5,8,6];

// Animation steps: which edges to draw for KTV1 (orange) and KTV2 (purple)
const STEPS = [
  {
    title:'Bài toán đầu vào',
    desc:'Đọc N=3, K=2. Đồ thị có 4 node: depot (0) và 3 khách hàng. Ma trận khoảng cách và thời gian phục vụ đã sẵn sàng. Mọi node được vẽ, chưa có tuyến đường nào.',
    stateHdr:'Trạng thái dữ liệu',
    state:`<div class="state-row"><span class="state-key">N, K</span><span class="state-val">3 khách hàng, 2 kỹ thuật viên</span></div>
    <div class="state-row"><span class="state-key">d[]</span><span class="state-val">[0, 5, 8, 6] phút phục vụ</span></div>
    <div class="state-row"><span class="state-key">matrix</span><span class="state-val">ma trận 4×4 thời gian di chuyển</span></div>`,
    edges1:[], edges2:[], highlight:[], showConstraint:false, showResult:false
  },
  {
    title:'Khai báo biến x[i,j,k]',
    desc:'Tạo K×(N+1)×N = 2×4×3 = 24 biến BoolVar. Mỗi cạnh có thể có (mũi tên mờ) đều có một biến x tương ứng. Solver sẽ quyết định cái nào = 1.',
    stateHdr:'Biến được tạo',
    state:`<div class="state-row"><span class="state-key">x (tổng)</span><span class="state-val"><span class="hi">24 BoolVar</span> — 12 cho KTV1, 12 cho KTV2</span></div>
    <div class="state-row"><span class="state-key">y[1], y[2]</span><span class="state-val">2 IntVar trong [0, 79]</span></div>
    <div class="state-row"><span class="state-key">self_loop</span><span class="state-val">6 BoolVar (3 KH × 2 KTV)</span></div>
    <div class="state-row"><span class="state-key">z</span><span class="state-val">1 IntVar trong [0, 79] — mục tiêu</span></div>`,
    edges1:[], edges2:[], highlight:[], showAllEdges:true, showConstraint:false, showResult:false
  },
  {
    title:'Ràng buộc 1 — Mỗi KH phục vụ đúng 1 lần',
    desc:'Với mỗi KH j=1,2,3: tổng tất cả cạnh đi vào j (từ bất kỳ KTV nào) = 1. Ràng buộc đảm bảo không KH nào bị bỏ sót hoặc phục vụ 2 lần.',
    stateHdr:'Ràng buộc 1',
    state:`<div class="state-row"><span class="state-key">j=1</span><span class="state-val">∑x[i,1,k] = 1 &nbsp;<span class="hi">✓ áp dụng</span></span></div>
    <div class="state-row"><span class="state-key">j=2</span><span class="state-val">∑x[i,2,k] = 1 &nbsp;<span class="hi">✓ áp dụng</span></span></div>
    <div class="state-row"><span class="state-key">j=3</span><span class="state-val">∑x[i,3,k] = 1 &nbsp;<span class="hi">✓ áp dụng</span></span></div>`,
    constraint:'∑<sub>k,i</sub> x[i,<b>j</b>,k] = 1 &nbsp; với mọi j ∈ {1,2,3}',
    edges1:[], edges2:[], highlight:[1,2,3], showAllEdges:true, showConstraint:true, showResult:false
  },
  {
    title:'Ràng buộc 2 & 3 — Luồng & Circuit',
    desc:'Với mỗi KTV k: (a) mỗi node j có sum_cạnh_vào + self_loop = 1. (b) AddCircuit đảm bảo tất cả cạnh được chọn tạo đúng 1 vòng liên thông qua depot — không có subtour.',
    stateHdr:'Ràng buộc 2 & 3',
    state:`<div class="state-row"><span class="state-key">RB2 (KTV1)</span><span class="state-val">3 ràng buộc luồng cho KH 1,2,3</span></div>
    <div class="state-row"><span class="state-key">RB2 (KTV2)</span><span class="state-val">3 ràng buộc luồng cho KH 1,2,3</span></div>
    <div class="state-row"><span class="state-key">AddCircuit</span><span class="state-val"><span class="hi">2 chu trình</span> — 1 cho KTV1, 1 cho KTV2</span></div>`,
    constraint:'AddCircuit(arcs<sub>k</sub>) với k=1,2<br>→ Loại trừ subtour',
    edges1:[], edges2:[], highlight:[], showAllEdges:true, showConstraint:true, showResult:false
  },
  {
    title:'Solver thử phương án đầu tiên',
    desc:'Solver đề xuất phân công ban đầu (chưa tối ưu): KTV 1 phục vụ KH1+KH2, KTV 2 phục vụ KH3. Tuyến KTV1: 0→1→2→0. Tuyến KTV2: 0→3→0.',
    stateHdr:'Phương án thử — chưa tối ưu',
    state:`<div class="state-row"><span class="state-key">KTV 1</span><span class="state-val">0→1→2→0<br>y[1] = (10+5)+(12+8)+(15+0) = <span class="lo">50 phút</span></span></div>
    <div class="state-row"><span class="state-key">KTV 2</span><span class="state-val">0→3→0<br>y[2] = (20+6)+(20+0) = <span class="lo">46 phút</span></span></div>
    <div class="state-row"><span class="state-key">z = max</span><span class="state-val"><span class="lo">50 phút</span> — tiếp tục tối ưu...</span></div>`,
    edges1:[[0,1],[1,2],[2,0]], edges2:[[0,3],[3,0]], highlight:[], showConstraint:false, showResult:false
  },
  {
    title:'Tính workload y[k]',
    desc:'Với phân công trên, y[k] = ∑ x[i,j,k]×(matrix[i][j]+d[j]). Mỗi cạnh được đi đóng góp thời gian di chuyển + phục vụ. z = max(y[1], y[2]) = 50 phút. Solver cố tìm phân công tốt hơn.',
    stateHdr:'Tính workload chi tiết',
    state:`<div class="state-row"><span class="state-key">0→1 (k=1)</span><span class="state-val">matrix[0][1]+d[1] = 10+5 = 15</span></div>
    <div class="state-row"><span class="state-key">1→2 (k=1)</span><span class="state-val">matrix[1][2]+d[2] = 12+8 = 20</span></div>
    <div class="state-row"><span class="state-key">2→0 (k=1)</span><span class="state-val">matrix[2][0]+d[0] = 15+0 = 15</span></div>
    <div class="state-row"><span class="state-key">y[1]</span><span class="state-val"><span class="lo">15+20+15 = 50 phút</span></span></div>
    <div class="state-row"><span class="state-key">y[2]</span><span class="state-val"><span class="lo">26+20 = 46 phút</span></span></div>`,
    edges1:[[0,1],[1,2],[2,0]], edges2:[[0,3],[3,0]], highlight:[], showConstraint:false, showResult:false
  },
  {
    title:'Solver tìm phương án tốt hơn',
    desc:'Solver thử phân công mới: KTV 1 phục vụ KH1+KH3, KTV 2 phục vụ KH2. Tuyến KTV1: 0→1→3→0. Tuyến KTV2: 0→2→0.',
    stateHdr:'Phương án mới — solver thử',
    state:`<div class="state-row"><span class="state-key">KTV 1</span><span class="state-val">0→1→3→0<br>y[1] = (10+5)+(18+6)+(20+0) = <span class="lo">59 phút</span></span></div>
    <div class="state-row"><span class="state-key">KTV 2</span><span class="state-val">0→2→0<br>y[2] = (15+8)+(15+0) = <span class="hi">38 phút</span></span></div>
    <div class="state-row"><span class="state-key">z = max</span><span class="state-val"><span class="lo">59 phút</span> — tệ hơn, solver loại</span></div>`,
    edges1:[[0,1],[1,3],[3,0]], edges2:[[0,2],[2,0]], highlight:[], showConstraint:false, showResult:false
  },
  {
    title:'Nghiệm tối ưu được chứng minh',
    desc:'Sau khi duyệt tất cả phân công khả thi, solver chứng minh phương án KTV1: 0→1→2→0 và KTV2: 0→3→0 có z=50 là tối ưu. Không có phân công nào cho z < 50.',
    stateHdr:'Nghiệm tối ưu — OPTIMAL',
    state:`<div class="state-row"><span class="state-key">KTV 1</span><span class="state-val">0 → 1 → 2 → 0 &nbsp; <span class="hi">✓</span></span></div>
    <div class="state-row"><span class="state-key">y[1]</span><span class="state-val"><span class="hi">50 phút</span></span></div>
    <div class="state-row"><span class="state-key">KTV 2</span><span class="state-val">0 → 3 → 0 &nbsp; <span class="hi">✓</span></span></div>
    <div class="state-row"><span class="state-key">y[2]</span><span class="state-val"><span class="hi">46 phút</span></span></div>
    <div class="state-row"><span class="state-key">z (minimax)</span><span class="state-val"><span class="hi">50 phút — OPTIMAL ✓</span></span></div>`,
    edges1:[[0,1],[1,2],[2,0]], edges2:[[0,3],[3,0]], highlight:[], showConstraint:false, showResult:false, optimal:true
  },
  {
    title:'Xuất tuyến đường',
    desc:'Truy vết từng tuyến từ depot, theo các cạnh x[i,j,k]=1. In số node và danh sách node cho từng KTV. Kết quả hoàn chỉnh!',
    stateHdr:'Output',
    state:`<div class="state-row"><span class="state-key">K</span><span class="state-val">2</span></div>
    <div class="state-row"><span class="state-key">KTV 1</span><span class="state-val">len=4 &nbsp; route: <span class="hi">0 1 2 0</span></span></div>
    <div class="state-row"><span class="state-key">KTV 2</span><span class="state-val">len=3 &nbsp; route: <span class="hi">0 3 0</span></span></div>`,
    edges1:[[0,1],[1,2],[2,0]], edges2:[[0,3],[3,0]], highlight:[], showConstraint:false, showResult:true, optimal:true
  }
];

let currentStep = 0;

function drawGraph() {
  const canvas = document.getElementById('graphCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const DPR = window.devicePixelRatio || 1;
  const W = canvas.parentElement.clientWidth;
  const H = 320;
  canvas.width = W * DPR;
  canvas.height = H * DPR;
  canvas.style.width = W + 'px';
  canvas.style.height = H + 'px';
  ctx.scale(DPR, DPR);

  const step = STEPS[currentStep];
  const isDark = window.matchMedia('(prefers-color-scheme:dark)').matches;
  const bg = isDark ? '#2a2a28' : '#ffffff';
  const textClr = isDark ? '#e8e7e2' : '#1a1a18';
  const mutedClr = isDark ? 'rgba(255,255,255,0.07)' : 'rgba(0,0,0,0.06)';

  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, W, H);

  // Scale nodes to canvas
  const scaleX = W / 340;
  const scaleY = H / 480;
  const ns = NODES.map(n => ({...n, cx: n.x * scaleX, cy: n.y * scaleY}));

  // Draw all possible edges (muted) when showAllEdges
  if (step.showAllEdges) {
    for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) {
      if (i === j) continue;
      drawEdge(ctx, ns[i].cx, ns[i].cy, ns[j].cx, ns[j].cy, mutedClr, 1, false, false);
    }
  }

  // Draw KTV2 edges (purple)
  step.edges2.forEach(([a,b]) => {
    drawEdge(ctx, ns[a].cx, ns[a].cy, ns[b].cx, ns[b].cy, '#6c5ce7', 2.5, true, true, step.optimal);
  });
  // Draw KTV1 edges (amber/orange)
  step.edges1.forEach(([a,b]) => {
    drawEdge(ctx, ns[a].cx, ns[a].cy, ns[b].cx, ns[b].cy, '#ef9f27', 2.5, true, true, step.optimal);
  });

  // Draw nodes
  ns.forEach(n => {
    const isHighlighted = step.highlight && step.highlight.includes(n.id);
    const r = n.id === 0 ? 26 : 22;

    // Glow for highlighted
    if (isHighlighted) {
      ctx.beginPath();
      ctx.arc(n.cx, n.cy, r + 6, 0, Math.PI*2);
      ctx.fillStyle = 'rgba(108,92,231,0.18)';
      ctx.fill();
    }

    ctx.beginPath();
    ctx.arc(n.cx, n.cy, r, 0, Math.PI*2);
    ctx.fillStyle = n.color;
    ctx.fill();
    ctx.strokeStyle = isDark ? 'rgba(255,255,255,0.15)' : 'rgba(0,0,0,0.12)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Label
    ctx.fillStyle = '#fff';
    ctx.font = `bold ${n.id===0?13:12}px -apple-system,sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const lines = n.label.split('\n');
    if (lines.length === 2) {
      ctx.fillText(lines[0], n.cx, n.cy - 6);
      ctx.font = `10px -apple-system,sans-serif`;
      ctx.fillStyle = 'rgba(255,255,255,0.8)';
      ctx.fillText(lines[1], n.cx, n.cy + 7);
    } else {
      ctx.fillText(n.label, n.cx, n.cy);
    }

    // Edge weights label next to edges — draw matrix values on arcs
  });

  // Distance labels on edges being drawn
  const allEdges = [...step.edges1.map(e=>[...e,1]), ...step.edges2.map(e=>[...e,2])];
  allEdges.forEach(([a,b,k]) => {
    const mid = { x:(ns[a].cx+ns[b].cx)/2, y:(ns[a].cy+ns[b].cy)/2 };
    const offX = (ns[b].cy-ns[a].cy)*0.15;
    const offY = -(ns[b].cx-ns[a].cx)*0.15;
    const travel = MATRIX[a][b];
    const svc = b>0 ? D[b] : 0;
    ctx.save();
    ctx.fillStyle = isDark ? 'rgba(30,30,26,0.85)' : 'rgba(255,255,255,0.9)';
    const lx = mid.x+offX, ly = mid.y+offY;
    ctx.beginPath();
    ctx.roundRect(lx-22, ly-10, 44, 20, 4);
    ctx.fill();
    ctx.fillStyle = k===1 ? '#ef9f27' : '#6c5ce7';
    ctx.font = '10px SFMono-Regular,Consolas,monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(`${travel}+${svc}`, lx, ly);
    ctx.restore();
  });
}

function drawEdge(ctx, x1,y1, x2,y2, color, width, arrow, curved, thick=false) {
  ctx.save();
  ctx.strokeStyle = color;
  ctx.lineWidth = thick ? width+1 : width;
  ctx.globalAlpha = curved ? 1 : 0.5;

  const dx = x2-x1, dy = y2-y1;
  const len = Math.sqrt(dx*dx+dy*dy);
  const ux = dx/len, uy = dy/len;
  const r = 23;
  const sx = x1+ux*r, sy = y1+uy*r;
  const ex = x2-ux*r, ey = y2-uy*r;

  if (curved) {
    const cpx = (sx+ex)/2 - dy*0.18;
    const cpy = (sy+ey)/2 + dx*0.18;
    ctx.beginPath();
    ctx.moveTo(sx,sy);
    ctx.quadraticCurveTo(cpx,cpy,ex,ey);
    ctx.stroke();
    if (arrow) {
      const t = 0.85;
      const aqx = (1-t)*(1-t)*sx+2*(1-t)*t*cpx+t*t*ex;
      const aqy = (1-t)*(1-t)*sy+2*(1-t)*t*cpy+t*t*ey;
      const angle = Math.atan2(ey-aqy, ex-aqx);
      drawArrowHead(ctx, ex, ey, angle, color, width);
    }
  } else {
    ctx.beginPath();
    ctx.moveTo(sx,sy);
    ctx.lineTo(ex,ey);
    ctx.stroke();
  }
  ctx.restore();
}

function drawArrowHead(ctx, x, y, angle, color, w) {
  ctx.save();
  ctx.translate(x,y);
  ctx.rotate(angle);
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(0,0);
  ctx.lineTo(-7,-4);
  ctx.lineTo(-7,4);
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function stepAnim(dir) {
  currentStep = Math.max(0, Math.min(STEPS.length-1, currentStep+dir));
  updateAnim();
}

function updateAnim() {
  const step = STEPS[currentStep];
  const total = STEPS.length;

  document.getElementById('stepCounter').textContent = `Bước ${currentStep+1} / ${total}`;
  document.getElementById('stepProg').style.width = ((currentStep+1)/total*100)+'%';
  document.getElementById('stepTitle').textContent = step.title;
  document.getElementById('stepDesc').textContent = step.desc;
  document.getElementById('stateHdr').textContent = step.stateHdr;
  document.getElementById('stateBody').innerHTML = step.state;

  const cbox = document.getElementById('constraintBox');
  if (step.showConstraint && step.constraint) {
    cbox.style.display='block';
    document.getElementById('constraintCode').innerHTML = step.constraint;
  } else {
    cbox.style.display='none';
  }

  document.getElementById('resultBadge').style.display = step.showResult ? 'block' : 'none';
  document.getElementById('btnPrev').disabled = currentStep === 0;
  document.getElementById('btnNext').disabled = currentStep === total-1;
  document.getElementById('btnNext').textContent = currentStep === total-1 ? 'Hoàn thành ✓' : 'Tiếp theo →';

  drawGraph();
}

// Init
window.addEventListener('resize', () => { if(document.getElementById('page-anim').classList.contains('active')) drawGraph(); });
updateAnim();
</script>
</body>
</html>
<!-- INJECTED BY PATCH: tab 3 styles + HTML + JS -->
<style>
/* ══ TAB 3: BIẾN X ══ */
.xpage-wrap { max-width: 960px; margin: 0 auto; padding: 20px 24px 48px; }

/* top explanation banner */
.concept-banner {
  display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-bottom: 28px;
}
.cb-card {
  background: var(--surface); border: .5px solid var(--border2);
  border-radius: var(--r-lg); padding: 16px 18px;
}
.cb-step { font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .07em; color: var(--text3); margin-bottom: 6px; }
.cb-title { font-size: 13.5px; font-weight: 600; margin-bottom: 5px; }
.cb-body { font-size: 12.5px; color: var(--text2); line-height: 1.65; }
.cb-arrow { display: flex; align-items: center; justify-content: center;
  font-size: 22px; color: var(--text3); padding-top: 30px; }

/* grid of x vars */
.xgrid-section { margin-bottom: 24px; }
.xgrid-label { font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .07em; color: var(--text3); margin-bottom: 10px; }
.xgrid { display: flex; flex-wrap: wrap; gap: 6px; }
.xvar {
  font-family: 'SFMono-Regular', Consolas, monospace; font-size: 11px;
  padding: 5px 9px; border-radius: 6px; border: .5px solid var(--border2);
  background: var(--bg2); color: var(--text2); transition: all .25s;
  cursor: default; position: relative; white-space: nowrap; min-width: 90px;
  text-align: center;
}
.xvar .xval {
  display: inline-block; margin-left: 4px; font-weight: 700;
  font-size: 12px; transition: all .25s;
}
.xvar.trying {
  border-color: var(--amber-bd); background: var(--amber-bg);
  color: var(--amber-text); transform: scale(1.06);
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--amber) 30%, transparent);
}
.xvar.set1 {
  border-color: var(--green-bd); background: var(--green-bg); color: var(--green-text);
}
.xvar.set0 {
  border-color: var(--border); background: var(--bg); color: var(--text3);
}
.xvar.conflict {
  border-color: #e74c3c; background: #fdeaea; color: #c0392b;
  animation: shake .3s ease;
}
@keyframes shake {
  0%,100%{transform:translateX(0)} 25%{transform:translateX(-4px)} 75%{transform:translateX(4px)}
}
@media (prefers-color-scheme: dark) {
  .xvar.conflict { background: #3b1010; color: #f5aaaa; border-color: #c0392b; }
}

/* constraint checker */
.constraint-checker { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }
.cc-row {
  display: grid; grid-template-columns: auto 1fr auto; gap: 10px;
  align-items: center; padding: 9px 14px; border-radius: 8px;
  border: .5px solid var(--border); background: var(--bg2);
  font-size: 13px; transition: all .2s;
}
.cc-row.active { border-color: var(--amber-bd); background: var(--amber-bg); }
.cc-row.ok     { border-color: var(--green-bd); background: var(--green-bg); }
.cc-row.fail   { border-color: #e74c3c; background: #fdeaea; }
@media (prefers-color-scheme: dark) {
  .cc-row.fail { background: #3b1010; border-color: #c0392b; }
}
.cc-icon { font-size: 15px; width: 22px; text-align: center; }
.cc-text { font-size: 12.5px; line-height: 1.5; color: var(--text); }
.cc-text .cc-formula { font-family: 'SFMono-Regular',Consolas,monospace; font-size: 11.5px; }
.cc-status { font-size: 11px; font-weight: 600; white-space: nowrap; }
.cc-status.s-wait   { color: var(--text3); }
.cc-status.s-check  { color: var(--amber-text); }
.cc-status.s-ok     { color: var(--green-text); }
.cc-status.s-fail   { color: #c0392b; }

/* bottom panel: narrative + controls */
.xanim-layout { display: grid; grid-template-columns: 1fr 320px; gap: 20px; }
.narrative-box {
  background: var(--surface); border: .5px solid var(--border2);
  border-radius: var(--r-lg); padding: 18px 20px;
}
.narr-phase { font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .07em; color: var(--text3); margin-bottom: 5px; }
.narr-title { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.narr-body { font-size: 13.5px; line-height: 1.8; color: var(--text2); }
.narr-body strong { color: var(--text); }
.narr-body .ck  { display:inline-block;font-family:'SFMono-Regular',Consolas,monospace;font-size:11.5px;background:var(--bg2);border:.5px solid var(--border2);border-radius:4px;padding:1px 6px;color:var(--blue-text); }
.narr-body .ck-g{ color:var(--green-text);background:var(--green-bg);border-color:var(--green-bd); }
.narr-body .ck-a{ color:var(--amber-text);background:var(--amber-bg);border-color:var(--amber-bd); }
.narr-body .ck-r{ color:#c0392b;background:#fdeaea;border-color:#e74c3c; }

.xanim-controls { display:flex; align-items:center; gap:8px; margin-top:14px; }
.xprog { flex:1; height:4px; background:var(--bg3); border-radius:2px; overflow:hidden; }
.xprog-fill { height:100%; background:var(--blue); border-radius:2px; transition:width .3s; }

/* right: z tracker */
.z-tracker { background: var(--surface); border: .5px solid var(--border2);
  border-radius: var(--r-lg); padding: 16px 18px; }
.zt-label { font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .07em; color: var(--text3); margin-bottom: 10px; }
.zt-z { text-align: center; padding: 14px; border-radius: 10px;
  background: var(--bg2); margin-bottom: 12px; border: .5px solid var(--border); }
.zt-z-label { font-size: 11px; color: var(--text3); margin-bottom: 4px; }
.zt-z-val { font-size: 28px; font-weight: 700; color: var(--text);
  font-family: 'SFMono-Regular',Consolas,monospace; transition: all .3s; }
.zt-z-val.improved { color: var(--green-text); }
.zt-z-val.worse    { color: var(--amber-text); }
.zt-routes { display: flex; flex-direction: column; gap: 8px; }
.zt-route { padding: 10px 12px; border-radius: 8px; border: .5px solid var(--border);
  background: var(--bg2); font-size: 12.5px; }
.zt-route-label { font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .06em; margin-bottom: 3px; }
.zt-route-path { font-family: 'SFMono-Regular',Consolas,monospace; font-size: 12px; margin-bottom: 3px; }
.zt-route-time { font-size: 11.5px; }
.ktv1-color { color: #ef9f27; } .ktv2-color { color: #6c5ce7; }
@media (max-width:720px) {
  .concept-banner { grid-template-columns: 1fr; }
  .xanim-layout   { grid-template-columns: 1fr; }
}
</style>

<!-- TAB 3 PAGE -->
<div class="page" id="page-xvar">
<div class="xpage-wrap">

  <!-- Top concept cards -->
  <div style="padding-top:20px; margin-bottom:20px;">
    <div class="hero-badge" style="display:inline-block;margin-bottom:12px">Hiểu đúng về biến x</div>
    <h1 style="font-size:22px;font-weight:700;margin-bottom:8px">x[i,j,k] — "Ô trống" để solver tự điền</h1>
    <p style="font-size:14px;color:var(--text2);line-height:1.7;max-width:680px">Khi bạn viết <code style="font-family:monospace;font-size:13px;background:var(--bg2);padding:1px 6px;border-radius:4px">model.NewBoolVar()</code>, bạn chỉ đang tạo ra một ô trống. Bạn <strong>không điền</strong> vào đó. Solver sẽ tự thử các giá trị 0/1 cho từng ô, kiểm tra ràng buộc, và tìm bộ giá trị tốt nhất.</p>
  </div>

  <div class="concept-banner">
    <div class="cb-card">
      <div class="cb-step">Bước A — Bạn làm</div>
      <div class="cb-title">📋 Tạo "tờ giấy thi"</div>
      <div class="cb-body"><code style="font-family:monospace;font-size:12px">model.NewBoolVar("x[0][1][1]")</code><br><br>Tạo ra 24 ô trống. Chưa điền gì. Solver chưa chạy. Đây chỉ là <strong>khai báo tên biến</strong> và cho solver biết "biến này tồn tại, giá trị của nó là 0 hoặc 1".</div>
    </div>
    <div class="cb-card">
      <div class="cb-step">Bước B — Bạn làm</div>
      <div class="cb-title">📏 Viết đề bài lên tờ giấy</div>
      <div class="cb-body"><code style="font-family:monospace;font-size:12px">model.Add(sum(...) == 1)</code><br><br>Thêm ràng buộc — các "luật" mà bộ 24 giá trị phải thỏa mãn. Solver chưa chạy. Đây chỉ là <strong>mô tả điều kiện</strong>.</div>
    </div>
    <div class="cb-card">
      <div class="cb-step">Bước C — Solver làm</div>
      <div class="cb-title">🤖 Solver tự điền vào ô trống</div>
      <div class="cb-body"><code style="font-family:monospace;font-size:12px">solver.Solve(model)</code><br><br>Solver thử từng tổ hợp giá trị 0/1 cho 24 biến x, kiểm tra ràng buộc, loại bỏ nghiệm xấu, giữ nghiệm tốt — cho đến khi tìm ra bộ giá trị tối ưu.</div>
    </div>
  </div>

  <!-- X VAR GRID -->
  <div class="xgrid-section">
    <div class="xgrid-label">24 biến x — solver đang thử điền từng ô (N=3, K=2)</div>
    <div style="margin-bottom:8px;font-size:12px;color:var(--text3)">
      <span style="display:inline-block;width:10px;height:10px;background:var(--bg2);border:.5px solid var(--border2);border-radius:3px;margin-right:4px"></span>chưa biết &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--amber-bg);border:.5px solid var(--amber-bd);border-radius:3px;margin-right:4px"></span>đang thử &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--green-bg);border:.5px solid var(--green-bd);border-radius:3px;margin-right:4px"></span>= 1 (đi cạnh này) &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--bg);border:.5px solid var(--border);border-radius:3px;margin-right:4px"></span>= 0 (không đi)
    </div>
    <div style="margin-bottom:6px;font-size:11.5px;color:var(--text3);font-weight:600">KTV 1:</div>
    <div class="xgrid" id="xgrid-k1"></div>
    <div style="margin:10px 0 6px;font-size:11.5px;color:var(--text3);font-weight:600">KTV 2:</div>
    <div class="xgrid" id="xgrid-k2"></div>
  </div>

  <!-- Constraint checker -->
  <div style="margin-bottom:20px;">
    <div class="xgrid-label">Ràng buộc đang kiểm tra</div>
    <div class="constraint-checker" id="constraint-checker"></div>
  </div>

  <!-- Bottom: narrative + z tracker -->
  <div class="xanim-layout">
    <div>
      <div class="narrative-box">
        <div class="narr-phase" id="narr-phase">Giai đoạn 1</div>
        <div class="narr-title" id="narr-title">Bắt đầu</div>
        <div class="narr-body" id="narr-body">...</div>
      </div>
      <div class="xanim-controls">
        <button class="ctrl-btn" id="xBtnPrev" onclick="xStep(-1)" disabled>← Trước</button>
        <div class="xprog"><div class="xprog-fill" id="xProg" style="width:0%"></div></div>
        <button class="ctrl-btn primary" id="xBtnNext" onclick="xStep(1)">Tiếp →</button>
        <button class="ctrl-btn" onclick="xReset()" style="padding:8px 12px">↺</button>
      </div>
      <div style="font-size:11.5px;color:var(--text3);margin-top:8px" id="xStepNum">Bước 1 / 12</div>
    </div>
    <div class="z-tracker">
      <div class="zt-label">Bộ nhớ solver — nghiệm tốt nhất hiện tại</div>
      <div class="zt-z">
        <div class="zt-z-label">z = max workload (cần nhỏ nhất)</div>
        <div class="zt-z-val" id="zt-z-display">∞</div>
      </div>
      <div class="zt-routes" id="zt-routes">
        <div class="zt-route">
          <div class="zt-route-label ktv1-color">KTV 1</div>
          <div class="zt-route-path" id="zt-r1">— chưa có —</div>
          <div class="zt-route-time" id="zt-t1" style="color:var(--text3)"></div>
        </div>
        <div class="zt-route">
          <div class="zt-route-label ktv2-color">KTV 2</div>
          <div class="zt-route-path" id="zt-r2">— chưa có —</div>
          <div class="zt-route-time" id="zt-t2" style="color:var(--text3)"></div>
        </div>
      </div>
    </div>
  </div>

</div>
</div><!-- #page-xvar -->

<script>
/* ═══════════════════════════════════════════
   PATCH: add tab 3 to nav
═══════════════════════════════════════════ */
(function(){
  const tabs = document.querySelector('.nav-tabs');
  if (tabs && !document.getElementById('tab3btn')) {
    const btn = document.createElement('button');
    btn.id = 'tab3btn';
    btn.className = 'nav-tab';
    btn.textContent = '🎲 Biến x — Solver điền thế nào?';
    btn.onclick = function(){ switchPage('xvar', this); initXAnim(); };
    tabs.appendChild(btn);
  }
})();

/* ═══════════════════════════════════════════
   X ANIMATION DATA
═══════════════════════════════════════════ */
// All 12 arcs per KTV (i,j) pairs i!=j, i,j in 0..3
const ALL_ARCS = [];
for(let i=0;i<4;i++) for(let j=0;j<4;j++) if(i!==j) ALL_ARCS.push([i,j]);
// 12 arcs × 2 KTV = 24 vars total

// State per x variable: '' | 'trying' | 'set1' | 'set0'
let xState = { k1:{}, k2:{} }; // key: "i-j"
let xCurrentStep = 0;

const XSTEPS = [
  {
    phase:'Giai đoạn 1 — Khởi tạo',
    title:'Solver nhìn thấy 24 ô trống',
    body:'Bạn gọi <span class="ck">model.NewBoolVar()</span> 24 lần — tạo ra <strong>24 ô trống</strong>. Solver nhìn thấy một "tờ giấy thi" với 24 câu hỏi Yes/No: "KTV 1 có đi cạnh 0→1 không?", "KTV 1 có đi cạnh 0→2 không?", v.v. Chưa có giá trị nào được điền.',
    trying_k1:[], trying_k2:[], set1_k1:[], set1_k2:[], set0_k1:[], set0_k2:[],
    constraints:[
      {text:'∑x[i,j,1] + sl[j,1] = 1 (với mỗi j)', status:'wait'},
      {text:'∑x[i,j,2] + sl[j,2] = 1 (với mỗi j)', status:'wait'},
      {text:'AddCircuit — 1 chu trình / KTV', status:'wait'},
      {text:'y[k] = ∑x[i,j,k]·(dist+svc)', status:'wait'},
      {text:'z ≥ y[k] với mọi k', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'— chưa có —', r2:'— chưa có —', t1:'', t2:''
  },
  {
    phase:'Giai đoạn 2 — Solver bắt đầu Branch',
    title:'Thử x[0,1,1] = 1 (KTV 1 đi depot→KH1)',
    body:'Solver chọn 1 biến và thử giá trị 1 trước. Đặt <span class="ck-a">x[0,1,1] = 1</span> — giả sử KTV 1 xuất phát đến KH1. Đây là nhánh đầu tiên của Branch & Bound.',
    trying_k1:[], set1_k1:['0-1'], set1_k2:[], set0_k1:[], set0_k2:[],
    constraints:[
      {text:'KH1: cần 1 cạnh vào — x[0,1,1]=1 ✓', status:'ok'},
      {text:'∑x[i,j,2] + sl[j,2] = 1 (chưa kiểm tra)', status:'wait'},
      {text:'AddCircuit KTV1 — đang xây dựng...', status:'check'},
      {text:'y[1] đang tích lũy...', status:'wait'},
      {text:'z chưa xác định', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'0 → 1 → ?', r2:'— chưa có —', t1:'', t2:''
  },
  {
    phase:'Giai đoạn 2 — Branch tiếp',
    title:'Propagation: tự động suy ra các biến khác',
    body:'Vì x[0,1,1]=1 (KTV 1 đã đi từ depot đến KH1), ràng buộc AddCircuit <strong>tự động suy ra</strong>: x[0,j,1] với j≠1 phải = 0 (KTV 1 không thể rời depot đến chỗ khác nữa). Đây là <strong>Constraint Propagation</strong> — solver không phải thử, nó tự tính ra.',
    trying_k1:[], set1_k1:['0-1'], set0_k1:['0-2','0-3'],
    set1_k2:[], set0_k2:[],
    constraints:[
      {text:'KH1: x[0,1,1]=1 ✓ đã thỏa', status:'ok'},
      {text:'Propagation: x[0,2,1]=0, x[0,3,1]=0', status:'ok'},
      {text:'AddCircuit KTV1 — tiếp tục suy luận...', status:'check'},
      {text:'y[1] đang tích lũy...', status:'wait'},
      {text:'z chưa xác định', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'0 → 1 → ?', r2:'— chưa có —', t1:'Propagation tự động', t2:''
  },
  {
    phase:'Giai đoạn 2 — Branch tiếp',
    title:'Thử x[1,3,1] = 1 (KTV 1 đi KH1→KH3)',
    body:'Từ KH1, solver thử KTV 1 đi đến KH3 tiếp theo. Đặt <span class="ck-a">x[1,3,1] = 1</span>. Propagation tiếp tục: x[1,2,1] và x[1,0,1] bị ép = 0 (KTV 1 đã rời KH1 rồi, không thể rời lần nữa).',
    trying_k1:[], set1_k1:['0-1','1-3'], set0_k1:['0-2','0-3','1-2','1-0'],
    set1_k2:[], set0_k2:[],
    constraints:[
      {text:'KH1: x[0,1,1]=1 ✓', status:'ok'},
      {text:'KH3: x[1,3,1]=1 — đang kiểm tra...', status:'check'},
      {text:'AddCircuit KTV1: 0→1→3→? cần về depot', status:'check'},
      {text:'y[1] tạm: (10+5)+(18+6) = 39 phút', status:'check'},
      {text:'z chưa xác định', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'0 → 1 → 3 → ?', r2:'— chưa có —', t1:'tạm 39 phút...', t2:''
  },
  {
    phase:'Giai đoạn 2 — Hoàn thành KTV 1',
    title:'AddCircuit ép x[3,0,1] = 1 (KTV 1 về depot)',
    body:'KTV 1 đã đi 0→1→3. AddCircuit biết: để tạo chu trình hợp lệ, cạnh duy nhất có thể đi tiếp từ KH3 phải về depot. Solver <strong>không cần thử</strong> — nó tự suy ra x[3,0,1]=1 và x[3,2,1]=0. Tuyến KTV 1 hoàn chỉnh: <span class="ck-g">0→1→3→0</span>.',
    trying_k1:[], set1_k1:['0-1','1-3','3-0'], set0_k1:['0-2','0-3','1-2','1-0','3-1','3-2'],
    set1_k2:[], set0_k2:[],
    constraints:[
      {text:'KH1 ✓, KH3 ✓ — tuyến KTV1 hợp lệ', status:'ok'},
      {text:'AddCircuit KTV1: 0→1→3→0 ✓', status:'ok'},
      {text:'y[1] = (10+5)+(18+6)+(20+0) = 59 phút ✓', status:'ok'},
      {text:'KH2 vẫn chưa ai phục vụ — cần KTV 2', status:'check'},
      {text:'z chưa xác định', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'0 → 1 → 3 → 0', r2:'— đang phân công —', t1:'59 phút', t2:''
  },
  {
    phase:'Giai đoạn 3 — Phân công KTV 2',
    title:'Ràng buộc RB1 ép KTV 2 phải phục vụ KH2',
    body:'Ràng buộc RB1: mỗi KH phải có đúng 1 cạnh vào. KH1 và KH3 đã do KTV 1 phục vụ. <strong>KH2 chưa ai ghé</strong> — solver biết tổng cạnh vào KH2 hiện tại = 0, phải = 1 → KTV 2 <strong>bắt buộc</strong> phải ghé KH2. Không cần thử, tự suy ra.',
    trying_k1:[], set1_k1:['0-1','1-3','3-0'], set0_k1:['0-2','0-3','1-2','1-0','3-1','3-2'],
    set1_k2:['0-2'], set0_k2:[],
    constraints:[
      {text:'KH1 ✓, KH3 ✓ (KTV1)', status:'ok'},
      {text:'KH2: bắt buộc KTV2 phải ghé → x[0,2,2]=1', status:'ok'},
      {text:'AddCircuit KTV2: đang xây...', status:'check'},
      {text:'y[1]=59, y[2] đang tính...', status:'check'},
      {text:'z chưa xác định', status:'wait'},
    ],
    zVal:'∞', zClass:'', r1:'0 → 1 → 3 → 0', r2:'0 → 2 → ?', t1:'59 phút', t2:'tạm...'
  },
  {
    phase:'Giai đoạn 3 — Hoàn thành KTV 2',
    title:'AddCircuit ép KTV 2 về depot: x[2,0,2] = 1',
    body:'KTV 2 đã ghé KH2. AddCircuit suy ra: phải quay về depot → <span class="ck-g">x[2,0,2]=1</span>. Tuyến KTV 2 hoàn chỉnh: <span class="ck-g">0→2→0</span>. Tất cả 24 biến x đã được điền! Solver kiểm tra toàn bộ ràng buộc.',
    trying_k1:[], set1_k1:['0-1','1-3','3-0'], set0_k1:['0-2','0-3','1-2','1-0','3-1','3-2'],
    set1_k2:['0-2','2-0'], set0_k2:['0-1','0-3','1-2','3-2','2-1','2-3'],
    constraints:[
      {text:'KH1 ✓, KH2 ✓, KH3 ✓ — tất cả được phục vụ', status:'ok'},
      {text:'AddCircuit KTV1: 0→1→3→0 ✓', status:'ok'},
      {text:'AddCircuit KTV2: 0→2→0 ✓', status:'ok'},
      {text:'y[1]=59, y[2]=(15+8)+(15)=38 phút ✓', status:'ok'},
      {text:'z = max(59,38) = 59 — nghiệm đầu tiên!', status:'ok'},
    ],
    zVal:'59', zClass:'', r1:'0 → 1 → 3 → 0', r2:'0 → 2 → 0', t1:'59 phút', t2:'38 phút'
  },
  {
    phase:'Giai đoạn 4 — Solver tiếp tục tìm',
    title:'Backtrack — thử phân công khác (x[0,2,1]=1)',
    body:'z=59 là nghiệm đầu tiên. Solver hỏi: "Có phân công nào cho z < 59 không?" Nó quay lại (backtrack) và thử nhánh khác: KTV 1 đi 0→2 thay vì 0→1. Đặt <span class="ck-a">x[0,2,1]=1</span>, đặt lại x[0,1,1]=0.',
    trying_k1:[], set1_k1:['0-2'], set0_k1:['0-1','0-3'],
    set1_k2:[], set0_k2:[],
    constraints:[
      {text:'Thử nhánh mới: KTV1 đi depot→KH2 trước', status:'check'},
      {text:'KH2: x[0,2,1]=1 — KTV1 phục vụ KH2', status:'check'},
      {text:'AddCircuit KTV1: đang xây lại...', status:'check'},
      {text:'y[1] đang tính lại...', status:'wait'},
      {text:'Mục tiêu: tìm z < 59', status:'check'},
    ],
    zVal:'59', zClass:'', r1:'0 → 2 → ?', r2:'— chưa biết —', t1:'', t2:''
  },
  {
    phase:'Giai đoạn 4 — Nhánh thứ hai',
    title:'Solver tìm ra: nhánh này cho z=65 > 59, loại bỏ',
    body:'Solver hoàn thành nhánh: KTV1: 0→2→3→0 (y=15+8+14+6+20=63), KTV2: 0→1→0 (y=10+5+10=25). z=max(63,25)=63 > 59 — <span class="ck-r">tệ hơn!</span> Solver loại bỏ nhánh này ngay (pruning). Tiếp tục backtrack thử nhánh khác.',
    trying_k1:[], set1_k1:['0-2','2-3','3-0'], set0_k1:['0-1','0-3','2-0','2-1'],
    set1_k2:['0-1','1-0'], set0_k2:['0-2','0-3'],
    constraints:[
      {text:'KH1 ✓, KH2 ✓, KH3 ✓', status:'ok'},
      {text:'AddCircuit KTV1: 0→2→3→0 ✓', status:'ok'},
      {text:'AddCircuit KTV2: 0→1→0 ✓', status:'ok'},
      {text:'y[1]=63, y[2]=25', status:'ok'},
      {text:'z=63 > 59 — LOẠI BỎ (pruning) ✗', status:'fail'},
    ],
    zVal:'59', zClass:'', r1:'0→2→3→0 (loại)', r2:'0→1→0 (loại)', t1:'63 phút ✗', t2:'25 phút'
  },
  {
    phase:'Giai đoạn 4 — Nhánh tối ưu',
    title:'Thử KTV1: 0→1→2→0 / KTV2: 0→3→0 — z=50!',
    body:'Solver thử: KTV1 đi 0→1→2→0, KTV2 đi 0→3→0. Tính workload: y[1]=(10+5)+(12+8)+(15)=50, y[2]=(20+6)+(20)=46. z=max(50,46)=<strong>50</strong> &lt; 59 — <span class="ck-g">tốt hơn!</span> Cập nhật nghiệm tốt nhất.',
    trying_k1:[], set1_k1:['0-1','1-2','2-0'], set0_k1:['0-2','0-3','1-3','1-0','2-1','2-3','3-1','3-2'],
    set1_k2:['0-3','3-0'], set0_k2:['0-1','0-2','3-1','3-2'],
    constraints:[
      {text:'KH1 ✓, KH2 ✓, KH3 ✓', status:'ok'},
      {text:'AddCircuit KTV1: 0→1→2→0 ✓', status:'ok'},
      {text:'AddCircuit KTV2: 0→3→0 ✓', status:'ok'},
      {text:'y[1]=50, y[2]=46 ✓', status:'ok'},
      {text:'z=50 < 59 — CẬP NHẬT nghiệm tốt nhất! ✓', status:'ok'},
    ],
    zVal:'50', zClass:'improved', r1:'0 → 1 → 2 → 0', r2:'0 → 3 → 0', t1:'50 phút ✓', t2:'46 phút ✓'
  },
  {
    phase:'Giai đoạn 5 — Chứng minh tối ưu',
    title:'Solver duyệt nốt các nhánh còn lại — đều tệ hơn',
    body:'Solver tiếp tục backtrack và thử tất cả phân công còn lại. Mọi nhánh đều cho z ≥ 50. Không có nhánh nào cải thiện được nữa. Solver <strong>chứng minh được</strong> z=50 là tối ưu toàn cục — không thể phân công tốt hơn.',
    trying_k1:[], set1_k1:['0-1','1-2','2-0'], set0_k1:['0-2','0-3','1-3','1-0','2-1','2-3','3-1','3-2'],
    set1_k2:['0-3','3-0'], set0_k2:['0-1','0-2','3-1','3-2'],
    constraints:[
      {text:'Tất cả KH được phục vụ ✓', status:'ok'},
      {text:'Tất cả tuyến hợp lệ (không subtour) ✓', status:'ok'},
      {text:'Workload được tính đúng ✓', status:'ok'},
      {text:'y[1]=50, y[2]=46 ✓', status:'ok'},
      {text:'z=50 — OPTIMAL đã chứng minh ✓', status:'ok'},
    ],
    zVal:'50', zClass:'improved', r1:'0 → 1 → 2 → 0', r2:'0 → 3 → 0', t1:'50 phút ✓', t2:'46 phút ✓'
  },
  {
    phase:'Giai đoạn 6 — Đọc kết quả',
    title:'solver.Value(x[i,j,k]) — đọc ô đã được điền',
    body:'Solver đã điền xong 24 ô. Bây giờ bạn mới đọc giá trị: <span class="ck">solver.Value(x[0,1,1])</span> = 1, <span class="ck">solver.Value(x[1,2,1])</span> = 1... Code truy vết tuyến đường bằng cách đọc từng giá trị này. <strong>Tóm lại:</strong> bạn tạo ô trống → viết luật → solver điền → bạn đọc kết quả.',
    trying_k1:[], set1_k1:['0-1','1-2','2-0'], set0_k1:['0-2','0-3','1-3','1-0','2-1','2-3','3-1','3-2'],
    set1_k2:['0-3','3-0'], set0_k2:['0-1','0-2','3-1','3-2'],
    constraints:[
      {text:'solver.Value(x[0,1,1]) = 1 ✓', status:'ok'},
      {text:'solver.Value(x[1,2,1]) = 1 ✓', status:'ok'},
      {text:'solver.Value(x[2,0,1]) = 1 ✓', status:'ok'},
      {text:'solver.Value(x[0,3,2]) = 1 ✓', status:'ok'},
      {text:'solver.Value(x[3,0,2]) = 1 ✓', status:'ok'},
    ],
    zVal:'50', zClass:'improved', r1:'0 → 1 → 2 → 0', r2:'0 → 3 → 0', t1:'50 phút ✓', t2:'46 phút ✓'
  }
];

let xInitDone = false;

function initXAnim() {
  if (xInitDone) return;
  xInitDone = true;
  // Build grids
  const g1 = document.getElementById('xgrid-k1');
  const g2 = document.getElementById('xgrid-k2');
  ALL_ARCS.forEach(([i,j]) => {
    ['k1','k2'].forEach((k,ki) => {
      const el = document.createElement('div');
      el.className = 'xvar';
      el.id = `xv-${k}-${i}-${j}`;
      el.innerHTML = `x[${i},${j},${ki+1}]<span class="xval" id="xvv-${k}-${i}-${j}">?</span>`;
      (ki===0?g1:g2).appendChild(el);
    });
  });
  // Build constraint checker
  renderXStep(0);
}

function renderXStep(si) {
  const s = XSTEPS[si];
  const total = XSTEPS.length;
  // Update all xvar states
  ALL_ARCS.forEach(([i,j]) => {
    ['k1','k2'].forEach(k => {
      const el = document.getElementById(`xv-${k}-${i}-${j}`);
      const vl = document.getElementById(`xvv-${k}-${i}-${j}`);
      if (!el) return;
      const key = `${i}-${j}`;
      const s1 = k==='k1' ? s.set1_k1 : s.set1_k2;
      const s0 = k==='k1' ? s.set0_k1 : s.set0_k2;
      const st = k==='k1' ? (s.trying_k1||[]) : (s.trying_k2||[]);
      el.className = 'xvar';
      if (s1 && s1.includes(key)) { el.classList.add('set1'); vl.textContent='=1'; }
      else if (s0 && s0.includes(key)) { el.classList.add('set0'); vl.textContent='=0'; }
      else if (st && st.includes(key)) { el.classList.add('trying'); vl.textContent='?'; }
      else { vl.textContent='?'; }
    });
  });

  // Constraints
  const cc = document.getElementById('constraint-checker');
  cc.innerHTML = '';
  (s.constraints||[]).forEach(c => {
    const row = document.createElement('div');
    row.className = 'cc-row' + (c.status==='ok'?' ok':c.status==='fail'?' fail':c.status==='check'?' active':'');
    const icon = c.status==='ok'?'✅':c.status==='fail'?'❌':c.status==='check'?'🔍':'⏳';
    const stxt = c.status==='ok'?'Thỏa ✓':c.status==='fail'?'Vi phạm ✗':c.status==='check'?'Đang kiểm tra...':'Chờ';
    const scls = c.status==='ok'?'s-ok':c.status==='fail'?'s-fail':c.status==='check'?'s-check':'s-wait';
    row.innerHTML = `<div class="cc-icon">${icon}</div><div class="cc-text cc-formula">${c.text}</div><div class="cc-status ${scls}">${stxt}</div>`;
    cc.appendChild(row);
  });

  // Narrative
  document.getElementById('narr-phase').textContent = s.phase;
  document.getElementById('narr-title').textContent = s.title;
  document.getElementById('narr-body').innerHTML = s.body;

  // Z tracker
  const zEl = document.getElementById('zt-z-display');
  zEl.textContent = s.zVal;
  zEl.className = 'zt-z-val' + (s.zClass?' '+s.zClass:'');
  document.getElementById('zt-r1').textContent = s.r1;
  document.getElementById('zt-r2').textContent = s.r2;
  const t1El = document.getElementById('zt-t1');
  const t2El = document.getElementById('zt-t2');
  t1El.textContent = s.t1;
  t1El.style.color = s.t1.includes('✓') ? 'var(--green-text)' : s.t1.includes('✗') ? '#c0392b' : 'var(--text3)';
  t2El.textContent = s.t2;
  t2El.style.color = 'var(--text2)';

  // Progress
  document.getElementById('xProg').style.width = ((si+1)/total*100)+'%';
  document.getElementById('xStepNum').textContent = `Bước ${si+1} / ${total}`;
  document.getElementById('xBtnPrev').disabled = si===0;
  document.getElementById('xBtnNext').disabled = si===total-1;
  document.getElementById('xBtnNext').textContent = si===total-1 ? 'Hoàn thành ✓' : 'Tiếp →';
}

function xStep(dir) {
  xCurrentStep = Math.max(0, Math.min(XSTEPS.length-1, xCurrentStep+dir));
  renderXStep(xCurrentStep);
}

function xReset() {
  xCurrentStep = 0;
  renderXStep(0);
}
</script>

<!-- ═══════════════════════════════════════════════════════════════
     TABS 4, 5, 6: styles + pages + JS
═══════════════════════════════════════════════════════════════ -->
<style>
/* shared extras */
.p-wrap{max-width:960px;margin:0 auto;padding:20px 24px 48px}
.p-hero{margin-bottom:24px}
.p-badge{display:inline-block;font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;background:var(--blue-bg);color:var(--blue-text);border:.5px solid var(--blue-bd);margin-bottom:10px}
.p-h1{font-size:22px;font-weight:700;margin-bottom:8px}
.p-sub{font-size:14px;color:var(--text2);line-height:1.7;max-width:700px}
.sec-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--text3);margin:0 0 10px}

/* ── TAB 4: AddCircuit vs MTZ ── */
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:.5px solid var(--border2);border-radius:var(--r-lg);overflow:hidden;margin-bottom:20px}
.cg-hdr{padding:13px 18px;font-size:13px;font-weight:700;border-bottom:.5px solid var(--border2)}
.cg-hdr.mtz{background:#faeeda;color:#633806}
.cg-hdr.ac {background:#e1f5ee;color:#085041}
.cg-col{padding:16px 18px;font-size:13px;line-height:1.75;color:var(--text);border-right:.5px solid var(--border2)}
.cg-col:last-child{border-right:none}
.cg-row{display:contents}
.cg-row .cg-col{border-top:.5px solid var(--border)}
.cg-row:first-child .cg-col{border-top:none}
.cg-sep{grid-column:1/-1;padding:8px 18px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--text3);background:var(--bg2);border-top:.5px solid var(--border2)}

.code-mini{font-family:'SFMono-Regular',Consolas,monospace;font-size:12px;background:var(--code-bg);border-radius:6px;padding:10px 12px;margin:8px 0;color:#f8f8f2;line-height:1.7;overflow-x:auto}
.code-mini .k{color:#c792ea}.code-mini .f{color:#82aaff}.code-mini .s{color:#c3e88d}.code-mini .n{color:#f78c6c}.code-mini .c{color:#546e7a;font-style:italic}

.subtour-demo{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}
.sd-box{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:16px;text-align:center}
.sd-box canvas{display:block;margin:0 auto 8px}
.sd-title{font-size:12.5px;font-weight:600;margin-bottom:4px}
.sd-body{font-size:12px;color:var(--text2);line-height:1.6}
.bad-badge{display:inline-block;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;background:#fdeaea;color:#c0392b;border:.5px solid #e74c3c;margin-bottom:6px}
.ok-badge {display:inline-block;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;background:var(--green-bg);color:var(--green-text);border:.5px solid var(--green-bd);margin-bottom:6px}

/* ── TAB 5: Propagation ── */
.prop-layout{display:grid;grid-template-columns:1fr 320px;gap:20px}
.prop-chain{display:flex;flex-direction:column;gap:0}
.prop-step{display:flex;gap:0;align-items:stretch}
.ps-num{width:32px;flex-shrink:0;display:flex;flex-direction:column;align-items:center}
.ps-circle{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;color:#fff}
.ps-line{flex:1;width:2px;background:var(--border2);margin:3px auto}
.ps-body{flex:1;padding:0 0 18px 14px}
.ps-title{font-size:14px;font-weight:600;margin-bottom:5px}
.ps-desc{font-size:13px;color:var(--text2);line-height:1.7}
.ps-tag{display:inline-block;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;margin-bottom:5px}
.tag-trigger{background:var(--blue-bg);color:var(--blue-text);border:.5px solid var(--blue-bd)}
.tag-infer {background:var(--purple-bg);color:var(--purple-text);border:.5px solid var(--purple-bd)}
.tag-rb    {background:var(--amber-bg);color:var(--amber-text);border:.5px solid var(--amber-bd)}
.tag-ok    {background:var(--green-bg);color:var(--green-text);border:.5px solid var(--green-bd)}

.prop-side{display:flex;flex-direction:column;gap:12px}
.prop-vars{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:14px 16px}
.pv-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text3);margin-bottom:10px}
.pv-row{display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:.5px solid var(--border);font-size:12.5px}
.pv-row:last-child{border-bottom:none}
.pv-name{font-family:'SFMono-Regular',Consolas,monospace;font-size:11.5px;color:var(--blue-text)}
.pv-val{font-weight:700;font-size:12px}
.pv-unknown{color:var(--text3)}
.pv-one   {color:var(--green-text)}
.pv-zero  {color:var(--text3);text-decoration:line-through;opacity:.6}
.pv-infer {color:var(--purple-text)}

.prop-key-box{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:14px 16px}
.pkb-title{font-size:13px;font-weight:600;margin-bottom:8px}
.pkb-body{font-size:12.5px;color:var(--text2);line-height:1.7}

/* ── TAB 6: Nếu vi phạm ── */
.viol-tabs{display:flex;gap:6px;margin-bottom:16px;flex-wrap:wrap}
.vt-btn{font-size:12px;padding:6px 14px;border-radius:8px;border:.5px solid var(--border2);background:var(--bg2);color:var(--text2);cursor:pointer;font-family:inherit;transition:all .12s}
.vt-btn:hover{background:var(--bg3)}
.vt-btn.active{background:var(--text);color:var(--bg);border-color:var(--text)}
.viol-panel{display:none}.viol-panel.active{display:block}

.viol-card{background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);overflow:hidden;margin-bottom:14px}
.vc-hdr2{display:flex;align-items:center;gap:12px;padding:14px 18px;border-bottom:.5px solid var(--border2)}
.vc-icon2{font-size:20px}
.vc-meta{flex:1}
.vc-title2{font-size:14px;font-weight:600}
.vc-sub2{font-size:12px;color:var(--text2);margin-top:2px}
.vc-sev{font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px}
.sev-high{background:#fdeaea;color:#c0392b;border:.5px solid #e74c3c}
.sev-med {background:var(--amber-bg);color:var(--amber-text);border:.5px solid var(--amber-bd)}
.vc-body2{padding:16px 18px}
.scenario-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.sc-box{border-radius:8px;padding:13px 14px;font-size:13px;line-height:1.7}
.sc-bad{background:#fdeaea;border:.5px solid #e74c3c}
.sc-ok {background:var(--green-bg);border:.5px solid var(--green-bd)}
.sc-bad-t{font-size:10px;font-weight:700;color:#c0392b;text-transform:uppercase;letter-spacing:.05em;margin-bottom:5px}
.sc-ok-t {font-size:10px;font-weight:700;color:var(--green-text);text-transform:uppercase;letter-spacing:.05em;margin-bottom:5px}

@media(max-width:720px){
  .compare-grid{grid-template-columns:1fr}
  .subtour-demo{grid-template-columns:1fr}
  .prop-layout{grid-template-columns:1fr}
  .scenario-grid{grid-template-columns:1fr}
}
</style>

<!-- ══ TAB 4: AddCircuit vs MTZ ══ -->
<div class="page" id="page-mtz">
<div class="p-wrap">
  <div class="p-hero">
    <div class="p-badge">Câu hỏi hay gặp nhất</div>
    <h1 class="p-h1">Tại sao dùng AddCircuit thay vì MTZ?</h1>
    <p class="p-sub">MTZ (Miller-Tucker-Zemlin) là phương pháp cổ điển loại trừ subtour trong TSP. Code ban đầu dùng MTZ và chỉ pass 2/10 test (MLE). Sau khi đổi sang AddCircuit, kết quả cải thiện rõ rệt. Dưới đây là lý do tại sao.</p>
  </div>

  <!-- Subtour demo canvases -->
  <div class="sec-lbl">Subtour là gì — và hai cách loại trừ nó</div>
  <div class="subtour-demo">
    <div class="sd-box">
      <div class="bad-badge">❌ Subtour — sai</div>
      <canvas id="c-subtour" width="200" height="160"></canvas>
      <div class="sd-title">KTV 1 đi vòng 1→2→1</div>
      <div class="sd-body">Mỗi node đều có 1 cạnh vào/ra — nhưng vòng này không qua depot (0). Tuyến đường hoàn toàn vô nghĩa thực tế.</div>
    </div>
    <div class="sd-box">
      <div class="ok-badge">✅ Hợp lệ</div>
      <canvas id="c-valid" width="200" height="160"></canvas>
      <div class="sd-title">KTV 1 đi 0→1→2→0</div>
      <div class="sd-body">Vòng duy nhất qua depot. Đây là tuyến đường hợp lệ mà AddCircuit bắt buộc phải tạo ra.</div>
    </div>
  </div>

  <!-- Comparison table -->
  <div class="sec-lbl" style="margin-top:24px">So sánh chi tiết</div>
  <div class="compare-grid">
    <div class="cg-hdr mtz">⚠ MTZ — cách cũ</div>
    <div class="cg-hdr ac">✅ AddCircuit — cách mới</div>

    <div class="cg-sep">Cơ chế loại trừ subtour</div>
    <div class="cg-row">
      <div class="cg-col">Thêm biến phụ <span class="ck ck-a">u[i,k]</span> = thứ tự thăm node i. Ràng buộc: <span class="ck ck-a">u[i,k] − u[j,k] + N·x[i,j,k] ≤ N−1</span>. Nếu có subtour thì ràng buộc này bị vi phạm.</div>
      <div class="cg-col">Không cần biến phụ. OR-Tools có ràng buộc đặc biệt <span class="ck ck-g">AddCircuit</span> tích hợp sẵn — kiểm tra cấu trúc đồ thị trực tiếp, không qua bất đẳng thức.</div>
    </div>

    <div class="cg-sep">Số biến cần tạo</div>
    <div class="cg-row">
      <div class="cg-col">K × (N+1) × N biến x <strong>+ K × N biến u</strong><br><br>Ví dụ N=10, K=5: x = 550, u = 50 → <strong>600 biến</strong></div>
      <div class="cg-col">K × (N+1) × N biến x <strong>+ K × N biến self_loop</strong> (BoolVar, nhẹ hơn IntVar nhiều)<br><br>Ví dụ N=10, K=5: x = 550, sl = 50 → <strong>600 biến</strong> nhưng nhẹ hơn vì sl là BoolVar</div>
    </div>

    <div class="cg-sep">Loại biến</div>
    <div class="cg-row">
      <div class="cg-col"><span class="ck ck-a">u[i,k]</span> là <strong>IntVar</strong> với domain [0, N]. Mỗi IntVar tiêu tốn bộ nhớ O(N) để lưu domain.<br><br>Nếu code dùng <span class="ck ck-a">NewIntVar(0,1)</span> cho cả x — đây chính là nguyên nhân MLE!</div>
      <div class="cg-col"><span class="ck ck-g">self_loop[i,k]</span> là <strong>BoolVar</strong> — chỉ cần 1 bit, không có domain phức tạp. CP-SAT xử lý BoolVar cực kỳ hiệu quả so với IntVar.</div>
    </div>

    <div class="cg-sep">Sức mạnh propagation</div>
    <div class="cg-row">
      <div class="cg-col">Ràng buộc tuyến tính — solver phải thử nhiều nhánh trước khi phát hiện subtour. <strong>Propagation yếu</strong>.</div>
      <div class="cg-col">AddCircuit dùng thuật toán đồ thị chuyên dụng (strongly connected components). Phát hiện subtour sớm hơn nhiều. <strong>Propagation mạnh</strong> → cắt nhánh sớm → ít backtrack hơn.</div>
    </div>

    <div class="cg-sep">Kết quả thực tế (bài BSRM N=10, K=5)</div>
    <div class="cg-row">
      <div class="cg-col" style="color:#c0392b">❌ 2/10 test pass<br>8 test MLE (Memory Limit Exceeded)<br>IntVar(0,1) thay vì BoolVar → bộ nhớ tăng gấp 10-20x</div>
      <div class="cg-col" style="color:var(--green-text)">✅ Pass nhiều test hơn<br>Không còn MLE trên test nhỏ-vừa<br>BoolVar + AddCircuit → bộ nhớ giảm đáng kể</div>
    </div>
  </div>

  <!-- Code comparison -->
  <div class="sec-lbl" style="margin-top:24px">Code thực tế — 3 thay đổi chính</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
    <div>
      <div style="font-size:12px;font-weight:600;color:var(--amber-text);margin-bottom:6px">Trước (MTZ)</div>
      <div class="code-mini"><span class="c"># x là IntVar(0,1) — sai type!</span>
x[i,j,k] = model.<span class="f">NewIntVar</span>(<span class="n">0</span>,<span class="n">1</span>,...)

<span class="c"># Biến thứ tự MTZ</span>
u[i,k] = model.<span class="f">NewIntVar</span>(<span class="n">0</span>,<span class="n">N</span>,...)

<span class="c"># Ràng buộc MTZ</span>
model.<span class="f">Add</span>(
  u[i,k] - u[j,k] + N*x[i,j,k]
  &lt;= N - <span class="n">1</span>
)</div>
    </div>
    <div>
      <div style="font-size:12px;font-weight:600;color:var(--green-text);margin-bottom:6px">Sau (AddCircuit)</div>
      <div class="code-mini"><span class="c"># x là BoolVar — đúng!</span>
x[i,j,k] = model.<span class="f">NewBoolVar</span>(...)

<span class="c"># self_loop thay MTZ</span>
self_loop[i,k] = model.<span class="f">NewBoolVar</span>(...)

<span class="c"># Một dòng thay cả MTZ</span>
model.<span class="f">AddCircuit</span>(arcs)</div>
    </div>
  </div>

  <!-- Why BoolVar matters -->
  <div style="background:var(--surface);border:.5px solid var(--border2);border-radius:var(--r-lg);padding:18px 20px;margin-top:16px">
    <div class="sec-lbl">Tại sao IntVar(0,1) gây MLE mà BoolVar thì không?</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-size:13.5px;line-height:1.75">
      <div>
        <strong style="color:var(--amber-text)">IntVar(0,1)</strong><br>
        CP-SAT lưu domain dạng tập các khoảng: <span class="ck ck-a">{[0,0], [1,1]}</span>. Mỗi IntVar cần metadata, pointer, domain list. Với K×N²= hàng nghìn biến → hàng MB bộ nhớ chỉ cho metadata.<br><br>
        Ngoài ra, solver tạo thêm các <em>literals</em> nội bộ để encode domain — IntVar(0,1) tạo ra 2–4 literals, nặng hơn BoolVar nhiều.
      </div>
      <div>
        <strong style="color:var(--green-text)">BoolVar</strong><br>
        CP-SAT lưu BoolVar dưới dạng 1 <em>literal SAT</em> duy nhất. Không có domain list, không có metadata phức tạp. Bộ nhớ gần như bằng 1 bit.<br><br>
        Solver có đường code path tối ưu riêng cho BoolVar — propagation nhanh hơn, ít allocate memory hơn. Đây là lý do <strong>NewBoolVar() luôn ưu tiên hơn NewIntVar(0,1)</strong> khi biến chỉ cần 0/1.
      </div>
    </div>
  </div>
</div>
</div>

<!-- ══ TAB 5: Propagation ══ -->
<div class="page" id="page-prop">
<div class="p-wrap">
  <div class="p-hero">
    <div class="p-badge" style="background:var(--purple-bg);color:var(--purple-text);border-color:var(--purple-bd)">Cơ chế ẩn</div>
    <h1 class="p-h1">Constraint Propagation — Solver tự suy ra thế nào?</h1>
    <p class="p-sub">Khi solver gán một biến, nó không chỉ đơn giản ghi giá trị đó xuống. Nó <strong>truyền thông tin</strong> qua các ràng buộc để tự động suy ra giá trị của nhiều biến khác — mà không cần phải thử. Đây là sức mạnh cốt lõi của CP-SAT.</p>
  </div>

  <div class="prop-layout">
    <!-- Chain -->
    <div>
      <div class="sec-lbl">Ví dụ N=3, K=2 — Solver gán x[0,1,1]=1 và hệ quả domino</div>
      <div class="prop-chain">

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--blue)">1</div><div class="ps-line"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-trigger">Trigger ban đầu</div>
            <div class="ps-title">Solver quyết định: x[0,1,1] = 1</div>
            <div class="ps-desc">KTV 1 đi từ depot (0) đến KH1 (1). Đây là quyết định đầu tiên trong nhánh Branch & Bound. Solver <strong>chọn</strong> giá trị này để thử.</div>
            <div class="code-mini" style="margin-top:8px">x[<span class="n">0</span>,<span class="n">1</span>,<span class="n">1</span>] = <span class="n">1</span>  <span class="c"># KTV1 đi depot→KH1</span></div>
          </div>
        </div>

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--purple)">2</div><div class="ps-line"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-infer">Suy ra từ AddCircuit</div>
            <div class="ps-title">AddCircuit tự ép x[0,2,1]=0 và x[0,3,1]=0</div>
            <div class="ps-desc">AddCircuit biết: mỗi node chỉ có thể có <strong>đúng 1 cạnh ra</strong> trong chu trình. Depot (0) đã có cạnh ra đến KH1 → tự động loại các cạnh ra khác từ depot của KTV1. Solver <strong>không cần thử</strong> — nó tự biết.</div>
            <div class="code-mini" style="margin-top:8px">x[<span class="n">0</span>,<span class="n">2</span>,<span class="n">1</span>] = <span class="n">0</span>  <span class="c"># tự động suy ra</span>
x[<span class="n">0</span>,<span class="n">3</span>,<span class="n">1</span>] = <span class="n">0</span>  <span class="c"># tự động suy ra</span></div>
          </div>
        </div>

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--amber)">3</div><div class="ps-line"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-rb">Từ Ràng buộc 2 (flow)</div>
            <div class="ps-title">self_loop[1,2] = 0 tự động (KTV2 không thể bỏ qua KH1)</div>
            <div class="ps-desc">RB1 nói: KH1 phải có đúng 1 cạnh vào tổng cộng. x[0,1,1]=1 đã thỏa RB1 cho KH1 → mọi cạnh vào KH1 của KTV2 phải = 0 → self_loop[1,2] = 1 (KTV2 bỏ qua KH1). Không cần thử.</div>
            <div class="code-mini" style="margin-top:8px"><span class="c"># KH1 đã được KTV1 phục vụ</span>
x[<span class="n">0</span>,<span class="n">1</span>,<span class="n">2</span>] = <span class="n">0</span>  <span class="c"># KTV2 không thể đến KH1</span>
x[<span class="n">2</span>,<span class="n">1</span>,<span class="n">2</span>] = <span class="n">0</span>
x[<span class="n">3</span>,<span class="n">1</span>,<span class="n">2</span>] = <span class="n">0</span>
self_loop[<span class="n">1</span>,<span class="n">2</span>] = <span class="n">1</span>  <span class="c"># KTV2 bỏ qua KH1</span></div>
          </div>
        </div>

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--blue)">4</div><div class="ps-line"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-trigger">Solver chọn tiếp</div>
            <div class="ps-title">Solver quyết định: x[1,3,1] = 1</div>
            <div class="ps-desc">Từ KH1, solver thử KTV1 đi đến KH3. Đây là quyết định chủ động thứ hai — chỉ còn 2 lựa chọn (KH2 hoặc KH3) vì KH1 đã rồi.</div>
          </div>
        </div>

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--purple)">5</div><div class="ps-line"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-infer">Suy ra từ AddCircuit</div>
            <div class="ps-title">AddCircuit ép x[3,0,1] = 1 — KTV1 phải về depot!</div>
            <div class="ps-desc">KTV1 đã đi 0→1→3. AddCircuit biết: 2 node còn lại (2) có self_loop. Chỉ còn depot (0) chưa được visit. Node 3 phải có cạnh ra về 0. → <strong>x[3,0,1]=1 được suy ra hoàn toàn tự động</strong>, không cần thử.</div>
            <div class="code-mini" style="margin-top:8px">x[<span class="n">3</span>,<span class="n">0</span>,<span class="n">1</span>] = <span class="n">1</span>  <span class="c"># bắt buộc — KTV1 về depot</span>
x[<span class="n">3</span>,<span class="n">1</span>,<span class="n">1</span>] = <span class="n">0</span>  <span class="c"># suy ra</span>
x[<span class="n">3</span>,<span class="n">2</span>,<span class="n">1</span>] = <span class="n">0</span>  <span class="c"># suy ra</span></div>
          </div>
        </div>

        <div class="prop-step">
          <div class="ps-num"><div class="ps-circle" style="background:var(--green)">6</div><div class="ps-line" style="display:none"></div></div>
          <div class="ps-body">
            <div class="ps-tag tag-ok">Kết quả</div>
            <div class="ps-title">Từ 2 quyết định → 22 biến còn lại được suy ra tự động</div>
            <div class="ps-desc">Solver chỉ thực sự <strong>"chọn"</strong> 2 biến (x[0,1,1] và x[1,3,1]). 22 biến còn lại được propagation suy ra. Đây là lý do CP-SAT nhanh hơn brute force tổ hợp 2²⁴ = 16 triệu lần thử rất nhiều.</div>
          </div>
        </div>

      </div><!-- .prop-chain -->
    </div>

    <!-- Side panel -->
    <div class="prop-side">
      <div class="prop-vars">
        <div class="pv-label">Trạng thái 24 biến x — sau 2 quyết định</div>
        <div class="pv-row"><span class="pv-name">x[0,1,1]</span><span class="pv-val pv-one">= 1 ✓ (chọn)</span></div>
        <div class="pv-row"><span class="pv-name">x[0,2,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[0,3,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[1,3,1]</span><span class="pv-val pv-one">= 1 ✓ (chọn)</span></div>
        <div class="pv-row"><span class="pv-name">x[1,0,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[1,2,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[3,0,1]</span><span class="pv-val pv-infer">= 1 (bắt buộc!)</span></div>
        <div class="pv-row"><span class="pv-name">x[3,1,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[3,2,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[2,*,1]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[*,1,2]</span><span class="pv-val pv-zero">= 0 (suy ra)</span></div>
        <div class="pv-row"><span class="pv-name">x[0,2,2]</span><span class="pv-val pv-unknown">? (chưa biết)</span></div>
        <div class="pv-row"><span class="pv-name">x[0,3,2]</span><span class="pv-val pv-unknown">? (chưa biết)</span></div>
      </div>
      <div class="prop-key-box">
        <div class="pkb-title">🔑 Takeaway quan trọng</div>
        <div class="pkb-body">
          <strong>Solver không brute-force.</strong> Mỗi lần "thử" 1 biến, propagation tự suy ra hàng chục biến khác. Không gian tìm kiếm bị thu hẹp theo cấp số nhân.<br><br>
          <strong>AddCircuit đặc biệt mạnh</strong> vì nó encode toàn bộ cấu trúc đồ thị — suy ra được nhiều hệ quả hơn so với các ràng buộc tuyến tính rời rạc.<br><br>
          <strong>BoolVar giúp propagation nhanh hơn</strong> — solver có code path tối ưu riêng cho literal SAT, nhanh hơn IntVar nhiều.
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ══ TAB 6: Nếu vi phạm ══ -->
<div class="page" id="page-viol">
<div class="p-wrap">
  <div class="p-hero">
    <div class="p-badge" style="background:var(--amber-bg);color:var(--amber-text);border-color:var(--amber-bd)">Hiểu qua phản ví dụ</div>
    <h1 class="p-h1">Nếu bỏ một ràng buộc — điều gì xảy ra?</h1>
    <p class="p-sub">Cách hiểu sâu nhất là xem điều gì xảy ra khi <strong>thiếu</strong> từng ràng buộc. Mỗi ràng buộc bảo vệ một điều kiện cụ thể — bỏ đi thì solver tạo ra nghiệm sai theo cách riêng của nó.</p>
  </div>

  <div class="viol-tabs">
    <button class="vt-btn active" onclick="showViol('rb1',this)">Bỏ Ràng buộc 1</button>
    <button class="vt-btn" onclick="showViol('rb2',this)">Bỏ Ràng buộc 2</button>
    <button class="vt-btn" onclick="showViol('circuit',this)">Bỏ AddCircuit</button>
    <button class="vt-btn" onclick="showViol('workload',this)">Sai Workload</button>
    <button class="vt-btn" onclick="showViol('minimax',this)">Sai Minimax</button>
  </div>

  <!-- RB1 -->
  <div class="viol-panel active" id="vp-rb1">
    <div class="viol-card">
      <div class="vc-hdr2">
        <div class="vc-icon2">❌</div>
        <div class="vc-meta">
          <div class="vc-title2">Bỏ ràng buộc 1: ∑x[i,j,k] = 1</div>
          <div class="vc-sub2">Ràng buộc: mỗi KH phải được phục vụ đúng 1 lần</div>
        </div>
        <div class="vc-sev sev-high">Nghiêm trọng</div>
      </div>
      <div class="vc-body2">
        <p style="font-size:13.5px;color:var(--text2);margin-bottom:12px">Không có ràng buộc này, solver được tự do bỏ sót hoặc phân công trùng lặp. Nó sẽ chọn bất kỳ phân công nào cho z nhỏ nhất — kể cả không hợp lệ.</p>
        <div class="scenario-grid">
          <div class="sc-box sc-bad">
            <div class="sc-bad-t">❌ Nghiệm sai có thể xảy ra</div>
            KTV 1: 0→1→2→0 (phục vụ KH1, KH2)<br>
            KTV 2: 0→1→3→0 (<strong>KH1 bị phục vụ 2 lần!</strong>)<br>
            KH3: không ai ghé (?)<br><br>
            z = rất nhỏ vì solver "gian lận" — bỏ KH3, tải ít hơn
          </div>
          <div class="sc-box sc-ok">
            <div class="sc-ok-t">✅ Có ràng buộc 1</div>
            Solver bắt buộc: mỗi KH có đúng 1 cạnh vào.<br><br>
            Không thể phục vụ 2 lần. Không thể bỏ sót. Mọi KH đều được phục vụ đúng 1 lần bởi đúng 1 KTV.
          </div>
        </div>
        <div style="background:var(--bg2);border-radius:8px;padding:12px 14px;font-size:13px;line-height:1.7;color:var(--text2)">
          <strong style="color:var(--text)">Thực tế:</strong> Nếu bỏ RB1, solver trả về z = 0 hoặc rất nhỏ (vì có thể bỏ sót mọi KH) hoặc tạo ra phân công trùng. Kết quả pass checker về format nhưng sai về logic hoàn toàn.
        </div>
      </div>
    </div>
  </div>

  <!-- RB2 -->
  <div class="viol-panel" id="vp-rb2">
    <div class="viol-card">
      <div class="vc-hdr2">
        <div class="vc-icon2">❌</div>
        <div class="vc-meta">
          <div class="vc-title2">Bỏ ràng buộc 2: ∑x[i,j,k] + self_loop[j,k] = 1</div>
          <div class="vc-sub2">Ràng buộc flow bảo toàn cho từng KTV</div>
        </div>
        <div class="vc-sev sev-high">AddCircuit lỗi ngay</div>
      </div>
      <div class="vc-body2">
        <p style="font-size:13.5px;color:var(--text2);margin-bottom:12px">Nếu bỏ RB2, self_loop không được quản lý đúng. AddCircuit nhận arcs có self_loop tự do → có thể tạo ra chu trình sai hoặc solver báo INFEASIBLE vô lý.</p>
        <div class="scenario-grid">
          <div class="sc-box sc-bad">
            <div class="sc-bad-t">❌ Không có RB2</div>
            self_loop[2,1] = 0 và x[*,2,1] = 0 đồng thời<br>→ Node 2 không có cạnh vào nào trong đồ thị KTV1<br>→ AddCircuit <strong>không thể tạo chu trình</strong><br>→ Solver báo INFEASIBLE dù bài toán có nghiệm!
          </div>
          <div class="sc-box sc-ok">
            <div class="sc-ok-t">✅ Có RB2</div>
            Với mọi cặp (j,k): tổng cạnh vào + self_loop = 1.<br><br>
            Đảm bảo mọi node luôn có đúng 1 "đại diện" trong arcs của AddCircuit — dù KTV k có ghé hay không.
          </div>
        </div>
        <div style="background:var(--bg2);border-radius:8px;padding:12px 14px;font-size:13px;line-height:1.7;color:var(--text2)">
          <strong style="color:var(--text)">Thực tế:</strong> Đây là lý do self_loop phải đi kèm RB2. Thiếu một trong hai đều làm AddCircuit hỏng. Chúng là bộ đôi không thể tách rời.
        </div>
      </div>
    </div>
  </div>

  <!-- Circuit -->
  <div class="viol-panel" id="vp-circuit">
    <div class="viol-card">
      <div class="vc-hdr2">
        <div class="vc-icon2">❌</div>
        <div class="vc-meta">
          <div class="vc-title2">Bỏ AddCircuit — chỉ giữ flow RB1 + RB2</div>
          <div class="vc-sub2">Không có ràng buộc chống subtour</div>
        </div>
        <div class="vc-sev sev-high">Subtour xuất hiện</div>
      </div>
      <div class="vc-body2">
        <p style="font-size:13.5px;color:var(--text2);margin-bottom:12px">RB1+RB2 chỉ đảm bảo mỗi node có đúng 1 cạnh vào/ra — không đảm bảo tất cả tạo thành 1 vòng duy nhất qua depot. Solver có thể tạo subtour.</p>
        <div class="scenario-grid">
          <div class="sc-box sc-bad">
            <div class="sc-bad-t">❌ Subtour — nghiệm sai</div>
            KTV 1 tạo vòng: 1→2→1 (không qua depot)<br>
            KTV 2 tạo vòng: 0→3→0<br><br>
            Node 1 có 1 cạnh vào (từ 2), 1 cạnh ra (đến 2) → RB thỏa ✓<br>
            Nhưng depot (0) không được đi qua! Tuyến vô nghĩa.
          </div>
          <div class="sc-box sc-ok">
            <div class="sc-ok-t">✅ Có AddCircuit</div>
            Tất cả cạnh được chọn phải tạo đúng 1 chu trình Hamiltonian.<br><br>
            Không thể có vòng nhỏ không qua depot. Depot luôn là điểm xuất phát và kết thúc của mỗi tuyến.
          </div>
        </div>
        <div style="background:var(--bg2);border-radius:8px;padding:12px 14px;font-size:13px;line-height:1.7;color:var(--text2)">
          <strong style="color:var(--text)">Thực tế:</strong> Nếu chỉ dùng RB1+RB2 mà không có AddCircuit, solver có thể tạo ra các "nghiệm" trông có vẻ hợp lệ về format nhưng KTV không bao giờ về depot. Hệ quả: in ra route nhưng truy vết sẽ bị lỗi hoặc tạo vòng vô tận.
        </div>
      </div>
    </div>
  </div>

  <!-- Workload -->
  <div class="viol-panel" id="vp-workload">
    <div class="viol-card">
      <div class="vc-hdr2">
        <div class="vc-icon2">⚠️</div>
        <div class="vc-meta">
          <div class="vc-title2">Lỗi thường gặp: d[j] if j != 0 else 0</div>
          <div class="vc-sub2">Quên kiểm tra depot khi tính workload</div>
        </div>
        <div class="vc-sev sev-med">Sai kết quả</div>
      </div>
      <div class="vc-body2">
        <p style="font-size:13.5px;color:var(--text2);margin-bottom:12px">Khi KTV quay về depot (cạnh j→0), không có thời gian phục vụ tại depot. Nếu quên điều kiện này và dùng d[0]=0 thì may mắn vẫn đúng — nhưng nếu d[0] vô tình có giá trị thì sai.</p>
        <div class="scenario-grid">
          <div class="sc-box sc-bad">
            <div class="sc-bad-t">❌ Thiếu kiểm tra</div>
            <code style="font-size:12px;font-family:monospace">service = d[j]</code><br><br>
            Nếu d = [0, 5, 8, 6]: d[0]=0 → may mắn đúng<br>
            Nhưng logic không rõ ràng — dễ bug khi thay đổi input
          </div>
          <div class="sc-box sc-ok">
            <div class="sc-ok-t">✅ Đúng cách</div>
            <code style="font-size:12px;font-family:monospace">service = d[j] if j != 0 else 0</code><br><br>
            Tường minh: depot không có thời gian phục vụ. Code tự giải thích, không phụ thuộc vào giá trị d[0].
          </div>
        </div>
        <div style="background:var(--bg2);border-radius:8px;padding:12px 14px;font-size:13px;line-height:1.7;color:var(--text2)">
          <strong style="color:var(--text)">Ví dụ số:</strong> KTV đi tuyến 0→1→3→0. Cạnh 3→0: matrix[3][0]=20, d[0]=0.<br>
          Đúng: service = 0 (về depot không phục vụ ai) → đóng góp 20 phút.<br>
          Nếu d[0] = 5 (giả sử): service sai = 5 → đóng góp 25 phút → y[k] sai → z sai.
        </div>
      </div>
    </div>
  </div>

  <!-- Minimax -->
  <div class="viol-panel" id="vp-minimax">
    <div class="viol-card">
      <div class="vc-hdr2">
        <div class="vc-icon2">⚠️</div>
        <div class="vc-meta">
          <div class="vc-title2">Nhầm: Minimize(sum(y)) thay vì Minimize(z)</div>
          <div class="vc-sub2">Min-sum vs Min-max — hai bài toán khác nhau hoàn toàn</div>
        </div>
        <div class="vc-sev sev-med">Sai mục tiêu</div>
      </div>
      <div class="vc-body2">
        <p style="font-size:13.5px;color:var(--text2);margin-bottom:12px">Đây là lỗi logic phổ biến nhất. Code chạy được, không báo lỗi, nhưng <strong>giải sai bài toán</strong>. Kết quả trông hợp lý nhưng không tối ưu theo đúng tiêu chí.</p>
        <div class="scenario-grid">
          <div class="sc-box sc-bad">
            <div class="sc-bad-t">❌ Minimize(sum(y)) — sai bài</div>
            Tối thiểu tổng thời gian làm việc.<br><br>
            Nghiệm có thể: y[1]=80, y[2]=5 → sum=85<br>
            Hoặc: y[1]=50, y[2]=45 → sum=95<br><br>
            Solver chọn phương án 1 (sum nhỏ hơn) → KTV1 làm 80 phút, KTV2 nghỉ gần hết! <strong>Không cân bằng tải.</strong>
          </div>
          <div class="sc-box sc-ok">
            <div class="sc-ok-t">✅ Minimize(z) với z≥y[k] — đúng</div>
            Tối thiểu workload của người bận nhất.<br><br>
            Nghiệm: y[1]=50, y[2]=46 → z=50<br>
            Thay vì: y[1]=80, y[2]=5 → z=80<br><br>
            Solver chọn z=50 vì nhỏ hơn → phân công <strong>công bằng hơn</strong>.
          </div>
        </div>
        <div style="background:var(--bg2);border-radius:8px;padding:12px 14px;font-size:13px;line-height:1.7;color:var(--text2)">
          <strong style="color:var(--text)">Tóm lại:</strong> Balanced Staff Routing yêu cầu <em>min-max makespan</em> — cân bằng tải. Min-sum tối ưu tổng hiệu suất nhưng không quan tâm ai làm nhiều nhất. Hai tiêu chí cho hai nghiệm hoàn toàn khác nhau.
        </div>
      </div>
    </div>
  </div>

</div>
</div>

<script>
/* inject tabs 4, 5, 6 into nav */
(function(){
  const tabs = document.querySelector('.nav-tabs');
  if (!tabs) return;
  const defs = [
    {id:'tab4btn', page:'mtz',  label:'⚖ AddCircuit vs MTZ'},
    {id:'tab5btn', page:'prop', label:'⚡ Propagation'},
    {id:'tab6btn', page:'viol', label:'💥 Nếu vi phạm'}
  ];
  defs.forEach(d => {
    if (document.getElementById(d.id)) return;
    const btn = document.createElement('button');
    btn.id = d.id; btn.className = 'nav-tab';
    btn.textContent = d.label;
    const page = d.page;
    const extra = d.page === 'mtz' ? drawSubtourCanvases : null;
    btn.onclick = function(){ switchPage(page, this); if(extra) extra(); };
    tabs.appendChild(btn);
  });
})();

/* violation tab switcher */
function showViol(id, btn) {
  document.querySelectorAll('.viol-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.vt-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('vp-'+id).classList.add('active');
  if (btn) btn.classList.add('active');
}

/* draw subtour canvases */
function drawSubtourCanvases() {
  drawSubtour('c-subtour');
  drawValid('c-valid');
}
function nodePos(id, w, h) {
  const pos = [{x:.5,y:.15},{x:.15,y:.75},{x:.85,y:.75},{x:.5,y:.92}];
  return {x:pos[id].x*w, y:pos[id].y*h};
}
function drawCanvas(cid, edges, colors, label) {
  const c = document.getElementById(cid); if (!c) return;
  const ctx = c.getContext('2d');
  const W=c.width, H=c.height;
  const isDark = window.matchMedia('(prefers-color-scheme:dark)').matches;
  ctx.fillStyle = isDark?'#2a2a28':'#fff'; ctx.fillRect(0,0,W,H);
  const ns = [0,1,2,3].map(i=>nodePos(i,W,H));
  const nc = ['#378add','#1d9e75','#1d9e75','#1d9e75'];
  // draw edges
  edges.forEach(([a,b,col]) => {
    const dx=ns[b].x-ns[a].x, dy=ns[b].y-ns[a].y, len=Math.sqrt(dx*dx+dy*dy);
    const ux=dx/len,uy=dy/len; const r=18;
    ctx.save(); ctx.strokeStyle=col; ctx.lineWidth=2.2; ctx.globalAlpha=.9;
    ctx.beginPath();
    const sx=ns[a].x+ux*r, sy=ns[a].y+uy*r;
    const ex=ns[b].x-ux*r, ey=ns[b].y-uy*r;
    const cpx=(sx+ex)/2-dy*.2, cpy=(sy+ey)/2+dx*.2;
    ctx.moveTo(sx,sy); ctx.quadraticCurveTo(cpx,cpy,ex,ey); ctx.stroke();
    // arrow
    const t=.85, aqx=(1-t)*(1-t)*sx+2*(1-t)*t*cpx+t*t*ex, aqy=(1-t)*(1-t)*sy+2*(1-t)*t*cpy+t*t*ey;
    const ang=Math.atan2(ey-aqy,ex-aqx);
    ctx.translate(ex,ey); ctx.rotate(ang); ctx.fillStyle=col;
    ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(-7,-4); ctx.lineTo(-7,4); ctx.closePath(); ctx.fill();
    ctx.restore();
  });
  // draw nodes
  ns.forEach((n,i) => {
    ctx.beginPath(); ctx.arc(n.x,n.y,18,0,Math.PI*2);
    ctx.fillStyle=nc[i]; ctx.fill();
    ctx.fillStyle='#fff'; ctx.font='bold 12px sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText(i===0?'D':i, n.x, n.y);
  });
}
function drawSubtour(cid) {
  drawCanvas(cid,[
    [1,2,'#ef9f27'],[2,1,'#ef9f27'],[0,3,'#6c5ce7'],[3,0,'#6c5ce7']
  ]);
}
function drawValid(cid) {
  drawCanvas(cid,[
    [0,1,'#ef9f27'],[1,2,'#ef9f27'],[2,0,'#ef9f27'],[0,3,'#6c5ce7'],[3,0,'#6c5ce7']
  ]);
}
</script>

<!-- ═══════════════════════════════════════════════════════
     TAB 7: SELF_LOOP — style giống hệt tab biến x
═══════════════════════════════════════════════════════ -->
<style>
/* reuse xvar styles, thêm sl-specific */
.sl-analogy {
  display: grid; grid-template-columns: 1fr auto 1fr; gap: 0;
  align-items: stretch; margin-bottom: 20px;
  border: .5px solid var(--border2); border-radius: var(--r-lg); overflow: hidden;
}
.sl-side { padding: 18px 20px; font-size: 13px; line-height: 1.75; }
.sl-side.bad { background: #fdeaea; border-right: .5px solid var(--border2); }
.sl-side.ok  { background: var(--green-bg); border-left: .5px solid var(--border2); }
@media (prefers-color-scheme: dark) {
  .sl-side.bad { background: #3b1010; }
  .sl-side.ok  { background: var(--ok-bg, #04342c); }
}
.sl-mid { display: flex; align-items: center; justify-content: center;
  padding: 0 16px; font-size: 22px; color: var(--text3);
  background: var(--bg2); border-left: .5px solid var(--border2); border-right: .5px solid var(--border2);
}
.sl-head { font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .06em; margin-bottom: 8px; }
.sl-head.bad { color: #c0392b; } .sl-head.ok { color: var(--green-text); }

/* sl grid items — same style as xvar but different color scheme */
.slvar {
  font-family: 'SFMono-Regular', Consolas, monospace; font-size: 11px;
  padding: 5px 9px; border-radius: 6px; border: .5px solid var(--border2);
  background: var(--bg2); color: var(--text2); transition: all .25s;
  white-space: nowrap; min-width: 100px; text-align: center;
}
.slvar .slval { display: inline-block; margin-left: 4px; font-weight: 700; font-size: 12px; }
.slvar.sl-trying { border-color: var(--amber-bd); background: var(--amber-bg); color: var(--amber-text); transform: scale(1.06); box-shadow: 0 0 0 2px color-mix(in srgb,var(--amber) 30%,transparent); }
.slvar.sl-is1    { border-color: var(--amber-bd); background: var(--amber-bg); color: var(--amber-text); }
.slvar.sl-is0    { border-color: var(--green-bd); background: var(--green-bg); color: var(--green-text); }
.slvar.sl-infer1 { border-color: var(--purple-bd); background: var(--purple-bg); color: var(--purple-text); }
.slvar.sl-infer0 { border-color: var(--green-bd); background: var(--green-bg); color: var(--green-text); opacity:.7; }

/* circuit vis canvas */
.circuit-vis { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
.cv-box { background: var(--surface); border: .5px solid var(--border2); border-radius: var(--r-lg); padding: 12px; text-align: center; }
.cv-box canvas { display: block; margin: 0 auto 6px; }
.cv-title { font-size: 12px; font-weight: 600; margin-bottom: 3px; }
.cv-body  { font-size: 11.5px; color: var(--text2); line-height: 1.55; }
</style>

<!-- PAGE -->
<div class="page" id="page-selfloop">
<div class="xpage-wrap">

  <div style="padding-top:20px;margin-bottom:20px">
    <div class="p-badge" style="background:var(--amber-bg);color:var(--amber-text);border-color:var(--amber-bd)">Biến phụ trợ</div>
    <h1 class="p-h1" style="margin-top:10px">self_loop[i, k] — "Cạnh ảo" cho AddCircuit</h1>
    <p class="p-sub">Tương tự biến x, self_loop cũng là ô trống solver tự điền. Nhưng thay vì hỏi "KTV k có đi cạnh i→j không?", nó hỏi: <strong>"KTV k có BỎ QUA khách hàng i không?"</strong> Nếu bỏ qua → = 1, nếu ghé → = 0.</p>
  </div>

  <!-- Analogy card -->
  <div class="sec-lbl">Vấn đề self_loop giải quyết</div>
  <div class="sl-analogy">
    <div class="sl-side bad">
      <div class="sl-head bad">❌ Không có self_loop</div>
      KTV 1 phục vụ KH1 và KH3.<br>
      Trong đồ thị KTV 1, <strong>KH2 hoàn toàn trống</strong> — không có cạnh vào, không có cạnh ra.<br><br>
      AddCircuit yêu cầu: <em>mọi node phải có đúng 1 cạnh vào và 1 cạnh ra.</em><br><br>
      KH2 vi phạm → <strong>AddCircuit báo lỗi</strong>, dù bài toán hoàn toàn có nghiệm!
    </div>
    <div class="sl-mid">→</div>
    <div class="sl-side ok">
      <div class="sl-head ok">✅ Có self_loop[2,1] = 1</div>
      Thêm "cạnh ảo" KH2 → KH2 vào arcs của KTV 1.<br><br>
      Nói với AddCircuit: <em>"Node KH2 đã được xử lý — KTV 1 chỉ bỏ qua nó thôi."</em><br><br>
      KH2 có 1 cạnh vào (tự vòng) → thỏa yêu cầu AddCircuit → <strong>solver chạy đúng.</strong>
    </div>
  </div>

  <!-- Visual: arcs list -->
  <div class="circuit-vis">
    <div class="cv-box">
      <div class="bad-badge">❌ arcs KTV1 thiếu KH2</div>
      <canvas id="sl-c-bad" width="200" height="160"></canvas>
      <div class="cv-title">Node KH2 bị "mồ côi"</div>
      <div class="cv-body">arcs = [(0,1,x[0,1,1]), (1,3,x[1,3,1]), (3,0,x[3,0,1])]<br>KH2 không xuất hiện → AddCircuit lỗi</div>
    </div>
    <div class="cv-box">
      <div class="ok-badge">✅ arcs KTV1 đủ với self_loop</div>
      <canvas id="sl-c-ok" width="200" height="160"></canvas>
      <div class="cv-title">Mọi node đều có đại diện</div>
      <div class="cv-body">arcs = [..., <strong>(2,2,self_loop[2,1])</strong>]<br>KH2 tự vòng = được xử lý → hợp lệ ✓</div>
    </div>
  </div>

  <!-- SL VAR GRID -->
  <div class="xgrid-section" style="margin-top:20px">
    <div class="xgrid-label">6 biến self_loop — K×N = 2×3 = 6 biến (N=3, K=2)</div>
    <div style="margin-bottom:8px;font-size:12px;color:var(--text3)">
      <span style="display:inline-block;width:10px;height:10px;background:var(--bg2);border:.5px solid var(--border2);border-radius:3px;margin-right:4px"></span>chưa biết &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--amber-bg);border:.5px solid var(--amber-bd);border-radius:3px;margin-right:4px"></span>= 1 (KTV bỏ qua KH này) &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--green-bg);border:.5px solid var(--green-bd);border-radius:3px;margin-right:4px"></span>= 0 (KTV có ghé KH này) &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--purple-bg);border:.5px solid var(--purple-bd);border-radius:3px;margin-right:4px"></span>= 1 (suy ra tự động)
    </div>
    <div style="margin-bottom:6px;font-size:11.5px;color:var(--text3);font-weight:600">KTV 1:</div>
    <div class="xgrid" id="slgrid-k1"></div>
    <div style="margin:10px 0 6px;font-size:11.5px;color:var(--text3);font-weight:600">KTV 2:</div>
    <div class="xgrid" id="slgrid-k2"></div>
  </div>

  <!-- Constraint checker -->
  <div style="margin-bottom:20px">
    <div class="xgrid-label">Ràng buộc liên quan đang kiểm tra</div>
    <div class="constraint-checker" id="sl-constraint-checker"></div>
  </div>

  <!-- Bottom layout -->
  <div class="xanim-layout">
    <div>
      <div class="narrative-box">
        <div class="narr-phase" id="sl-narr-phase">Giai đoạn 1</div>
        <div class="narr-title" id="sl-narr-title">Bắt đầu</div>
        <div class="narr-body"  id="sl-narr-body">...</div>
      </div>
      <div class="xanim-controls">
        <button class="ctrl-btn" id="slBtnPrev" onclick="slStep(-1)" disabled>← Trước</button>
        <div class="xprog"><div class="xprog-fill" id="slProg" style="width:0%"></div></div>
        <button class="ctrl-btn primary" id="slBtnNext" onclick="slStep(1)">Tiếp →</button>
        <button class="ctrl-btn" onclick="slReset()" style="padding:8px 12px">↺</button>
      </div>
      <div style="font-size:11.5px;color:var(--text3);margin-top:8px" id="slStepNum">Bước 1 / 10</div>
    </div>

    <!-- right: relationship tracker -->
    <div class="z-tracker">
      <div class="zt-label">Mối quan hệ x ↔ self_loop</div>
      <div style="display:flex;flex-direction:column;gap:8px" id="sl-rel-box">
        <div style="padding:10px 12px;border-radius:8px;border:.5px solid var(--border);background:var(--bg2);font-size:12.5px">
          <div style="font-size:10px;font-weight:700;color:var(--text3);text-transform:uppercase;margin-bottom:4px">Quy tắc bù nhau</div>
          Với mỗi cặp (KH j, KTV k):<br>
          <span style="font-family:monospace;font-size:11.5px">∑x[i,j,k] + self_loop[j,k] = 1</span><br><br>
          → Nếu KTV k <strong>đến j</strong>: x=1, sl=0<br>
          → Nếu KTV k <strong>bỏ qua j</strong>: x=0, sl=1<br>
          → Không thể cả hai = 1 hoặc cả hai = 0
        </div>
        <div style="padding:10px 12px;border-radius:8px;border:.5px solid var(--border);background:var(--bg2);font-size:12.5px" id="sl-current-state">
          <div style="font-size:10px;font-weight:700;color:var(--text3);text-transform:uppercase;margin-bottom:6px">Trạng thái hiện tại</div>
          <div id="sl-state-rows">Chưa có thông tin...</div>
        </div>
      </div>
    </div>
  </div>

</div>
</div><!-- #page-selfloop -->

<script>
/* inject tab 7 */
(function(){
  const tabs = document.querySelector('.nav-tabs');
  if (!tabs || document.getElementById('tab7btn')) return;
  const btn = document.createElement('button');
  btn.id = 'tab7btn'; btn.className = 'nav-tab';
  btn.textContent = '🔁 self_loop';
  btn.onclick = function(){ switchPage('selfloop', this); initSLAnim(); };
  tabs.appendChild(btn);
})();

/* ── STEPS DATA ── */
const SL_STEPS = [
  {
    phase: 'Giai đoạn 1 — Vấn đề',
    title: 'AddCircuit cần mọi node có đủ cạnh vào/ra',
    body: 'Trước khi hiểu self_loop, cần hiểu yêu cầu của <span class="ck">AddCircuit</span>: trong đồ thị của mỗi KTV, <strong>mọi node (depot + tất cả KH) phải có đúng 1 cạnh vào và 1 cạnh ra</strong>. Nếu 1 node thiếu cạnh → AddCircuit báo lỗi ngay, kể cả khi bài toán có nghiệm hợp lệ.',
    sl_k1: {1:'?',2:'?',3:'?'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'AddCircuit: mọi node phải có đúng 1 cạnh vào/ra', status:'check'},
      {text:'∑x[i,j,k] + self_loop[j,k] = 1 (chưa áp)', status:'wait'},
      {text:'self_loop[j,k] = 1 − ∑x[i,j,k]', status:'wait'},
    ],
    stateRows: 'Tất cả self_loop chưa xác định...'
  },
  {
    phase: 'Giai đoạn 1 — Vấn đề',
    title: 'Nếu KTV 1 chỉ ghé KH1 và KH3 — KH2 bị bỏ trống',
    body: 'Giả sử solver đang thử: KTV 1 đi tuyến 0→1→3→0. Trong đồ thị KTV 1: node 0,1,3 đều có cạnh. Nhưng <strong>node KH2 (node 2) hoàn toàn không có cạnh nào</strong> → AddCircuit không thể tạo chu trình hợp lệ → INFEASIBLE dù tuyến thực tế đúng!',
    sl_k1: {1:'?',2:'?',3:'?'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'KTV1: node 0,1,3 có cạnh ✓', status:'ok'},
      {text:'KTV1: node 2 — không có cạnh nào ✗', status:'fail'},
      {text:'AddCircuit KTV1 → LỖI vì node 2 bị bỏ trống', status:'fail'},
    ],
    stateRows: '<span style="color:#c0392b">KH2 trong đồ thị KTV1: không có cạnh nào → AddCircuit lỗi!</span>'
  },
  {
    phase: 'Giai đoạn 2 — Giải pháp',
    title: 'Tạo self_loop[2,1] = "cạnh ảo" KH2→KH2 cho KTV1',
    body: 'Giải pháp: thêm một "cạnh ảo" từ KH2 về chính nó (self_loop) vào arcs của KTV 1. Khi solver điền <span class="ck-a">self_loop[2,1] = 1</span>, AddCircuit hiểu: "node KH2 đã được xử lý — KTV 1 đơn giản bỏ qua nó". Node KH2 giờ có đủ 1 cạnh vào/ra (cạnh ảo) → hợp lệ.',
    sl_k1: {1:'?',2:'1',3:'?'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'self_loop[2,1] = 1 → node 2 có cạnh ảo 2→2 ✓', status:'ok'},
      {text:'AddCircuit KTV1: node 0,1,2,3 đều có đại diện ✓', status:'ok'},
      {text:'∑x[i,2,1] + self_loop[2,1] = 0+1 = 1 ✓', status:'ok'},
    ],
    stateRows: '<span class="ck-a">self_loop[2,1] = 1</span> → KTV 1 bỏ qua KH2<br>Node KH2 trong đồ thị KTV1: cạnh ảo 2→2 ✓'
  },
  {
    phase: 'Giai đoạn 2 — Ràng buộc',
    title: 'Ràng buộc 2 liên kết x và self_loop: tổng = 1',
    body: 'Ràng buộc 2 đảm bảo x và self_loop <strong>bù nhau chính xác</strong>:<br><br><span class="ck">∑x[i,j,k] + self_loop[j,k] = 1</span><br><br>Nếu KTV k đến j (∑x = 1) → self_loop bắt buộc = 0.<br>Nếu KTV k bỏ qua j (∑x = 0) → self_loop bắt buộc = 1.<br><br>Không thể cả hai = 1 (vừa đến vừa bỏ qua) hay cả hai = 0 (không có gì).',
    sl_k1: {1:'?',2:'1',3:'?'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'RB2 (j=2,k=1): ∑x[i,2,1] + self_loop[2,1] = 0+1 = 1 ✓', status:'ok'},
      {text:'RB2 tổng quát: buộc sl=1−∑x cho mọi cặp (j,k)', status:'ok'},
      {text:'Nếu vi phạm: sl=1 mà vẫn có x=1 → tổng=2 ≠ 1 ✗', status:'wait'},
    ],
    stateRows: 'Quy tắc: <span class="ck-g">self_loop[j,k] = 1 − ∑x[i,j,k]</span><br>Hai biến luôn bù nhau, tổng = 1'
  },
  {
    phase: 'Giai đoạn 3 — Solver điền',
    title: 'Solver gán x[0,1,1]=1 → self_loop[1,1] tự động = 0',
    body: 'Solver quyết định KTV 1 đi đến KH1: <span class="ck-g">x[0,1,1]=1</span>. Ngay lập tức ràng buộc 2 propagate: ∑x[i,1,1] = 1 → self_loop[1,1] bắt buộc = 0. <strong>Solver không cần thử</strong> — nó tự suy ra self_loop[1,1]=0 vì KTV 1 có ghé KH1.',
    sl_k1: {1:'0',2:'?',3:'?'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'x[0,1,1]=1 → KTV1 ghé KH1 ✓', status:'ok'},
      {text:'RB2 (j=1,k=1): 1 + self_loop[1,1] = 1 → sl=0 (suy ra)', status:'ok'},
      {text:'self_loop[1,1]=0 → KTV1 KHÔNG bỏ qua KH1 ✓', status:'ok'},
    ],
    stateRows: '<span class="ck-g">self_loop[1,1] = 0</span> → KTV 1 có ghé KH1<br><span style="color:var(--text3);font-size:11px">Suy ra tự động từ x[0,1,1]=1</span>'
  },
  {
    phase: 'Giai đoạn 3 — Solver điền',
    title: 'Solver gán x[1,3,1]=1 → self_loop[3,1] tự động = 0',
    body: 'Tiếp tục: solver quyết định KTV 1 đi từ KH1→KH3: <span class="ck-g">x[1,3,1]=1</span>. Tương tự: ∑x[i,3,1]=1 → <span class="ck-g">self_loop[3,1]=0</span> tự động. KTV 1 có ghé KH3 → không bỏ qua → self_loop = 0.',
    sl_k1: {1:'0',2:'?',3:'0'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'x[1,3,1]=1 → KTV1 ghé KH3 ✓', status:'ok'},
      {text:'RB2 (j=3,k=1): 1 + self_loop[3,1] = 1 → sl=0 (suy ra)', status:'ok'},
      {text:'Còn lại: KH2 với KTV1 — chưa biết', status:'check'},
    ],
    stateRows: '<span class="ck-g">self_loop[1,1] = 0</span> → KTV1 ghé KH1<br><span class="ck-g">self_loop[3,1] = 0</span> → KTV1 ghé KH3<br><span class="ck-a">self_loop[2,1] = ?</span> → chưa biết'
  },
  {
    phase: 'Giai đoạn 3 — Suy ra tự động',
    title: 'KH2 chưa ai ghé → self_loop[2,1] = 1 bắt buộc',
    body: 'Ràng buộc 1 (RB1) đã đảm bảo KH2 được phục vụ bởi KTV 2. Vậy với KTV 1: ∑x[i,2,1] = 0 (KTV 1 không đến KH2). RB2 suy ra: 0 + self_loop[2,1] = 1 → <span class="ck-a">self_loop[2,1] = 1</span>. KTV 1 bỏ qua KH2 — cạnh ảo được bật lên để AddCircuit hợp lệ.',
    sl_k1: {1:'0',2:'1-infer',3:'0'}, sl_k2: {1:'?',2:'?',3:'?'},
    constraints:[
      {text:'RB1: KH2 do KTV2 phục vụ → x[*,2,1]=0', status:'ok'},
      {text:'RB2 (j=2,k=1): 0 + self_loop[2,1] = 1 → sl=1 (bắt buộc)', status:'ok'},
      {text:'AddCircuit KTV1: node 2 có cạnh ảo 2→2 ✓', status:'ok'},
    ],
    stateRows: '<span class="ck-g">self_loop[1,1] = 0</span> → KTV1 ghé KH1<br><span class="ck-p" style="color:var(--purple-text)">self_loop[2,1] = 1</span> → KTV1 bỏ qua KH2 (suy ra!)<br><span class="ck-g">self_loop[3,1] = 0</span> → KTV1 ghé KH3'
  },
  {
    phase: 'Giai đoạn 4 — KTV 2',
    title: 'KTV 2 phục vụ KH2 → self_loop[2,2] = 0, còn sl[1,2] và sl[3,2] = 1',
    body: 'KTV 2 đi tuyến 0→2→0. Solver gán x[0,2,2]=1 → <span class="ck-g">self_loop[2,2]=0</span>. KTV 2 không ghé KH1 và KH3 (đã do KTV 1 phục vụ) → <span class="ck-a">self_loop[1,2]=1</span> và <span class="ck-a">self_loop[3,2]=1</span> được suy ra tự động.',
    sl_k1: {1:'0',2:'1-infer',3:'0'}, sl_k2: {1:'1-infer',2:'0',3:'1-infer'},
    constraints:[
      {text:'x[0,2,2]=1 → KTV2 ghé KH2 → sl[2,2]=0 ✓', status:'ok'},
      {text:'KH1,KH3 đã do KTV1 → sl[1,2]=sl[3,2]=1 (suy ra) ✓', status:'ok'},
      {text:'AddCircuit KTV2: 0→2→0, node 1,3 tự vòng ✓', status:'ok'},
    ],
    stateRows: '<strong>KTV 2:</strong><br><span class="ck-a">self_loop[1,2] = 1</span> → KTV2 bỏ qua KH1<br><span class="ck-g">self_loop[2,2] = 0</span> → KTV2 ghé KH2<br><span class="ck-a">self_loop[3,2] = 1</span> → KTV2 bỏ qua KH3'
  },
  {
    phase: 'Giai đoạn 5 — Tổng kết',
    title: 'Tất cả 6 self_loop đã được điền — AddCircuit hoạt động',
    body: 'Toàn bộ 6 biến self_loop đã xác định. Mỗi giá trị đều được <strong>suy ra tự động</strong> từ các biến x qua ràng buộc 2 — solver không cần "thử" self_loop riêng. Self_loop chỉ là gương phản chiếu của x: x=1 thì sl=0, x=0 thì sl=1. Nhờ đó AddCircuit của cả 2 KTV đều hợp lệ.',
    sl_k1: {1:'0',2:'1-infer',3:'0'}, sl_k2: {1:'1-infer',2:'0',3:'1-infer'},
    constraints:[
      {text:'AddCircuit KTV1: 0→1→3→0, node 2 tự vòng ✓', status:'ok'},
      {text:'AddCircuit KTV2: 0→2→0, node 1,3 tự vòng ✓', status:'ok'},
      {text:'Tất cả 6 self_loop suy ra tự động từ x ✓', status:'ok'},
    ],
    stateRows: '<strong>KTV 1:</strong> sl[1,1]=0, <span style="color:var(--purple-text)">sl[2,1]=1</span>, sl[3,1]=0<br><strong>KTV 2:</strong> <span style="color:var(--purple-text)">sl[1,2]=1</span>, sl[2,2]=0, <span style="color:var(--purple-text)">sl[3,2]=1</span><br><br>Màu cam = bỏ qua · Màu xanh = có ghé · Tím = suy ra'
  },
  {
    phase: 'Giai đoạn 6 — Đọc kết quả',
    title: 'self_loop không xuất hiện trong output — chỉ dùng nội bộ',
    body: 'Khi truy vết route, code chỉ đọc <span class="ck">solver.Value(x[current,j,k])</span> để tìm cạnh tiếp theo — <strong>không đọc self_loop</strong>. Self_loop hoàn toàn là biến nội bộ phục vụ AddCircuit. Người dùng nhìn kết quả không thấy nó đâu cả — nhưng nếu thiếu nó, AddCircuit sẽ không chạy được.',
    sl_k1: {1:'0',2:'1-infer',3:'0'}, sl_k2: {1:'1-infer',2:'0',3:'1-infer'},
    constraints:[
      {text:'solver.Value(self_loop[*]) — không bao giờ được đọc', status:'ok'},
      {text:'Chỉ x[i,j,k] được đọc khi truy vết route', status:'ok'},
      {text:'self_loop = "cầu nối" giữa x và AddCircuit, không hơn', status:'ok'},
    ],
    stateRows: '<strong>Vai trò self_loop tóm gọn:</strong><br>• Tồn tại vì AddCircuit cần nó<br>• Giá trị luôn = 1 − ∑x (tự suy ra)<br>• Không bao giờ xuất hiện trong output<br>• Bỏ nó đi → AddCircuit lỗi ngay'
  }
];

const SL_NODES = [1,2,3]; // KH indices
let slCurrentStep = 0;
let slInitDone = false;

function initSLAnim() {
  if (slInitDone) return;
  slInitDone = true;
  // Build grids
  ['k1','k2'].forEach((k,ki) => {
    const g = document.getElementById(`slgrid-${k}`);
    SL_NODES.forEach(i => {
      const el = document.createElement('div');
      el.className = 'slvar';
      el.id = `slv-${k}-${i}`;
      el.innerHTML = `sl[${i},${ki+1}]<span class="slval" id="slvv-${k}-${i}">?</span>`;
      g.appendChild(el);
    });
  });
  // Draw canvases
  drawSLCanvas('sl-c-bad', false);
  drawSLCanvas('sl-c-ok',  true);
  renderSLStep(0);
}

function renderSLStep(si) {
  const s = SL_STEPS[si];
  const total = SL_STEPS.length;

  // update grids
  ['k1','k2'].forEach(k => {
    const map = k==='k1' ? s.sl_k1 : s.sl_k2;
    SL_NODES.forEach(i => {
      const el = document.getElementById(`slv-${k}-${i}`);
      const vl = document.getElementById(`slvv-${k}-${i}`);
      if (!el) return;
      el.className = 'slvar';
      const v = map[i];
      if      (v==='1')       { el.classList.add('sl-is1');    vl.textContent='=1'; }
      else if (v==='0')       { el.classList.add('sl-is0');    vl.textContent='=0'; }
      else if (v==='1-infer') { el.classList.add('sl-infer1'); vl.textContent='=1'; }
      else if (v==='0-infer') { el.classList.add('sl-infer0'); vl.textContent='=0'; }
      else                    { vl.textContent='?'; }
    });
  });

  // constraints
  const cc = document.getElementById('sl-constraint-checker');
  cc.innerHTML = '';
  (s.constraints||[]).forEach(c => {
    const row = document.createElement('div');
    row.className = 'cc-row'+(c.status==='ok'?' ok':c.status==='fail'?' fail':c.status==='check'?' active':'');
    const icon = c.status==='ok'?'✅':c.status==='fail'?'❌':c.status==='check'?'🔍':'⏳';
    const stxt = c.status==='ok'?'Thỏa ✓':c.status==='fail'?'Vi phạm ✗':c.status==='check'?'Đang kiểm tra...':'Chờ';
    const scls = c.status==='ok'?'s-ok':c.status==='fail'?'s-fail':c.status==='check'?'s-check':'s-wait';
    row.innerHTML = `<div class="cc-icon">${icon}</div><div class="cc-text cc-formula">${c.text}</div><div class="cc-status ${scls}">${stxt}</div>`;
    cc.appendChild(row);
  });

  // narrative
  document.getElementById('sl-narr-phase').textContent = s.phase;
  document.getElementById('sl-narr-title').textContent = s.title;
  document.getElementById('sl-narr-body').innerHTML = s.body;
  document.getElementById('sl-state-rows').innerHTML = s.stateRows;

  // progress
  document.getElementById('slProg').style.width = ((si+1)/total*100)+'%';
  document.getElementById('slStepNum').textContent = `Bước ${si+1} / ${total}`;
  document.getElementById('slBtnPrev').disabled = si===0;
  document.getElementById('slBtnNext').disabled = si===total-1;
  document.getElementById('slBtnNext').textContent = si===total-1?'Hoàn thành ✓':'Tiếp →';
}

function slStep(dir) {
  slCurrentStep = Math.max(0, Math.min(SL_STEPS.length-1, slCurrentStep+dir));
  renderSLStep(slCurrentStep);
}
function slReset() { slCurrentStep=0; renderSLStep(0); }

/* draw circuit canvases */
function drawSLCanvas(cid, withSelfLoop) {
  const c = document.getElementById(cid); if(!c) return;
  const ctx = c.getContext('2d');
  const W=c.width, H=c.height;
  const isDark = window.matchMedia('(prefers-color-scheme:dark)').matches;
  ctx.fillStyle = isDark?'#2a2a28':'#fff'; ctx.fillRect(0,0,W,H);
  // node positions: depot top-center, KH1 left, KH2 right, KH3 bottom
  const ns = [{x:100,y:28},{x:30,y:110},{x:170,y:110},{x:100,y:148}];
  const nc = ['#378add','#1d9e75','#1d9e75','#1d9e75'];
  const lbl = ['D','1','2','3'];

  // KTV1 edges: 0→1→3→0
  [[0,1],[1,3],[3,0]].forEach(([a,b]) => drawSLEdge(ctx,ns[a],ns[b],'#ef9f27'));

  // self_loop on node 2 if enabled
  if (withSelfLoop) {
    ctx.save();
    ctx.strokeStyle='#ef9f27'; ctx.lineWidth=2; ctx.setLineDash([3,3]);
    ctx.beginPath();
    ctx.arc(ns[2].x+22, ns[2].y, 12, 0, Math.PI*2);
    ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle='#ef9f27'; ctx.font='bold 9px sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText('sl=1', ns[2].x+22, ns[2].y);
    ctx.restore();
  } else {
    // show red X on node 2
    ctx.save();
    ctx.strokeStyle='#e74c3c'; ctx.lineWidth=2;
    const x=ns[2].x, y=ns[2].y;
    ctx.beginPath(); ctx.moveTo(x+14,y-14); ctx.lineTo(x+26,y-2); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(x+26,y-14); ctx.lineTo(x+14,y-2); ctx.stroke();
    ctx.restore();
  }

  // nodes
  ns.forEach((n,i) => {
    const r=i===0?16:14;
    ctx.beginPath(); ctx.arc(n.x,n.y,r,0,Math.PI*2);
    ctx.fillStyle = (i===2 && !withSelfLoop) ? '#e74c3c' : nc[i];
    ctx.fill();
    ctx.fillStyle='#fff'; ctx.font=`bold 11px sans-serif`; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText(lbl[i],n.x,n.y);
  });
}

function drawSLEdge(ctx,a,b,col) {
  const dx=b.x-a.x,dy=b.y-a.y,len=Math.sqrt(dx*dx+dy*dy);
  const ux=dx/len,uy=dy/len,r=15;
  const sx=a.x+ux*r,sy=a.y+uy*r,ex=b.x-ux*r,ey=b.y-uy*r;
  const cpx=(sx+ex)/2-dy*.25,cpy=(sy+ey)/2+dx*.25;
  ctx.save(); ctx.strokeStyle=col; ctx.lineWidth=2; ctx.globalAlpha=.9;
  ctx.beginPath(); ctx.moveTo(sx,sy); ctx.quadraticCurveTo(cpx,cpy,ex,ey); ctx.stroke();
  const t=.85,aqx=(1-t)*(1-t)*sx+2*(1-t)*t*cpx+t*t*ex,aqy=(1-t)*(1-t)*sy+2*(1-t)*t*cpy+t*t*ey;
  const ang=Math.atan2(ey-aqy,ex-aqx);
  ctx.translate(ex,ey); ctx.rotate(ang); ctx.fillStyle=col;
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(-6,-3); ctx.lineTo(-6,3); ctx.closePath(); ctx.fill();
  ctx.restore();
}
</script>
