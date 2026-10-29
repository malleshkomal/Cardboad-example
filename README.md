# ♻ Circular Carbon Toolkit

**LCA / Product Carbon Footprints, Scope 1-2-3 accounting and sustainable procurement for a circular paper value chain**

Recovered paper → recycled cartonboard → folding cartons & gypsum board

![Standard](https://img.shields.io/badge/ISO-14067%20%7C%2014040%2F44-1f4e3d)
![GHG Protocol](https://img.shields.io/badge/GHG%20Protocol-Scope%201%C2%B72%C2%B73-2a78d6)
![PACT](https://img.shields.io/badge/PACT-Data%20Quality%20Rating-1baf7a)
![Excel](https://img.shields.io/badge/Model-Excel%20%2B%20Python-217346)
![Data](https://img.shields.io/badge/data-fictional-lightgrey)

> **Interactive dashboard:** open [`docs/index.html`](docs/index.html) in a browser, or enable GitHub Pages (Settings → Pages → Branch `main`, folder `/docs`). It will then be live at [malleshkomal.github.io/Cardboad-example](https://malleshkomal.github.io/Cardboad-example/).

![Dashboard preview](assets/dashboard_preview.png)

---

## Contents

1. [What this project shows](#1-what-this-project-shows)
2. [Scope 1, 2 and 3 explained](#2-scope-1-2-and-3-explained)
3. [Results](#3-results)
4. [Product carbon footprints (LCA)](#4-product-carbon-footprints-lca)
5. [Supplier data & sustainable procurement](#5-supplier-data--sustainable-procurement)
6. [Decarbonisation levers](#6-decarbonisation-levers)
7. [How the model works](#7-how-the-model-works)
8. [Repository structure & how to run](#8-repository-structure--how-to-run)
9. [Methodology & limitations](#9-methodology--limitations)

---

## 1. What this project shows

The company is fictional. It runs a **circular business model**: it buys recovered paper (RCP), turns it into 100 % recycled cartonboard in its own mills, and sells the board externally. It also converts the board into **folding cartons** and uses it as **liner paper for gypsum board**. Trim waste from converting goes back to the mill, and used products return as recovered paper or recycled gypsum.

| Task | Where |
|---|---|
| Product Carbon Footprints (PCF) per ISO 14067 | `PCF_Board`, `PCF_FoldingCarton`, `PCF_GypsumBoard` |
| Corporate GHG inventory, Scope 1, 2 (location + market) and all 15 Scope 3 categories | `GHG_Inventory` |
| Collecting and validating supplier CO₂ data (PACT data quality rating) | `Supplier_Register` |
| Supplier ESG evaluation (EcoVadis themes + climate maturity) | `Supplier_Scorecard` |
| KPIs and scorecards for sustainable procurement | `KPI_Dashboard` |
| Decarbonisation potential and abatement cost (MACC) | `Decarbonisation` |
| Supplier survey and internal training programme | `Supplier_Survey`, `Training_Plan` |

---

## 2. Scope 1, 2 and 3 explained

The **GHG Protocol** sorts every tonne of CO₂ by one question: **whose chimney or exhaust does it come out of?**

- 🔵 **Scope 1**: our own chimneys and exhausts.
- 🟠 **Scope 2**: the power plant's chimney, for the electricity *we* buy.
- 🟢 **Scope 3**: everybody else's chimneys in our value chain: suppliers, hauliers and customers.

![Animated explainer of Scope 1, 2 and 3](assets/animated/scopes_explained.svg)

<sub>▶ The animation cycles Scope 1 → Scope 2 → Scope 3 every 15 s. The highlighted zone and the caption change together.</sub>

### 2.1 The footprint at a glance

![Animated breakdown of the footprint by scope and Scope 3 category](assets/animated/emissions_buildup.svg)

| Scope | Simple definition | What it is in this business | Result |
|---|---|---|---|
| 🔵 **Scope 1**: direct | Fuel burned in equipment **we own or control** | Natural gas in board-mill boilers/CHP, gypsum calcination & drying, forklift diesel | **202,029 t CO₂e** (40 %) |
| 🟠 **Scope 2**: purchased energy | Emissions at the power plant for **electricity/steam we buy** | Grid power for pulpers, board machines, printing presses | **107,900 t** market-based (21 %) · 84,232 t location-based |
| 🟢 **Scope 3**: value chain | **Everyone else's** emissions caused by our business (15 categories) | Starch, chemicals, gypsum, transport, fuel upstream, processing of sold board, end-of-life | **201,170 t** (39 %) |

> **How every number is calculated:** `activity data × emission factor = emissions`.
> Example: board mills burn **675.4 GWh** of natural gas × **0.201 kg CO₂e/kWh** = **135,764 t CO₂e**.

---

### 2.2 🔵 Scope 1: direct emissions (we own the chimney)

**What:** fuel burned on our sites, in our boilers, dryers, kilns and vehicles.
**Why it's the biggest scope here:** paper and gypsum board both need a lot of **heat to dry water out**, and that heat comes from natural gas.

| Source | Activity | × Factor | = t CO₂e | Share of S1 |
|---|---:|---:|---:|---:|
| Board mills: steam & drying (boilers/CHP) | 675.4 GWh gas | 0.201 kg/kWh | **135,764** | 67 % |
| Gypsum board plants: calcination + drying | 301.5 GWh gas | 0.201 kg/kWh | **60,602** | 30 % |
| Mobile equipment: forklifts, yard trucks | 1.5 million l diesel | 2.65 kg/l | **3,975** | 2 % |
| Folding carton plants: heating & ink drying | 8.4 GWh gas | 0.201 kg/kWh | **1,688** | 1 % |
| **Total Scope 1** | | | **202,029** | 100 % |

💡 **Levers:** heat pumps / mechanical vapour recompression (L02), electrode boiler on green power (L03), dryer heat recovery (L04), biomethane (L05). See [section 6](#6-decarbonisation-levers).

---

### 2.3 🟠 Scope 2: purchased electricity (someone else's chimney, our demand)

**What:** the CO₂ emitted at power plants to produce the **232 GWh** of electricity our mills and plants use.
**Special rule:** Scope 2 must be reported **two ways**, and the animation shows why they differ.

![Animated Scope 2 location-based vs market-based](assets/animated/scope2_methods.svg)

| Method | What it answers | Calculation | Result |
|---|---|---|---:|
| **Location-based** | "How dirty is the grid we're plugged into?" | 232 GWh × 0.363 kg/kWh (German grid mix) | 84,232 t |
| **Market-based** ✔ | "What electricity did we *contract* to buy?" | 25 % × 0 (Guarantees of Origin) + 75 % × 0.62 kg/kWh (residual mix) | **107,900 t** |

💡 **Why market-based is higher:** certified green power has already been claimed by its buyers, so the leftover "residual mix" is dirtier than the grid average. Buying more renewable power (L01: +50 % PPA) is the **single biggest lever in the whole model** at about 72,000 t/yr.

---

### 2.4 🟢 Scope 3: the value chain (everyone else's chimney)

**What:** emissions that happen *outside* our sites but are **caused by our business**. Upstream that means making our raw materials, trucking them in and producing our fuel. Downstream it means customers processing our board and disposing of products at end-of-life.

![Animated value chain with Scope 1, 2 and 3 boundaries](assets/animated/value_chain_flow.svg)

<sub>▶ Dashed arrows show material flowing through the chain. The blue band (our own operations) is Scope 1 + 2; the green bands are Scope 3. The green loop at the bottom is the circular economy: used paper and gypsum come back as raw material.</sub>

#### The 15 Scope 3 categories in this business

| # | Category | Status | What it means here | Method | t CO₂e |
|---|---|:---:|---|---|---:|
| 1 | Purchased goods & services | ✅ | Starch, chemicals, inks, gypsum, recovered paper, indirect spend | Hybrid: supplier PCFs + secondary + spend-based | 52,951 |
| 2 | Capital goods | ✅ | New machines and buildings | Spend-based | 12,250 |
| 3 | Fuel- & energy-related | ✅ | Producing and transporting our gas and power (well-to-tank, grid losses) | Average-data | 40,932 |
| 4 | Upstream transport | ✅ | Trucks bringing recovered paper and gypsum; our paid deliveries | Distance-based (t·km) | 26,626 |
| 5 | Waste in operations | ✅ | Pulper rejects (plastics) incinerated; wastewater | Average-data | 20,025 |
| 6 | Business travel | ✅ | Flights, trains, rental cars | Distance-based | 630 |
| 7 | Employee commuting | ✅ | 2,800 employees driving to work | Average-data | 3,599 |
| 8 | Upstream leased assets | ➖ | Already inside Scope 1/2 | Not relevant | – |
| 9 | Downstream transport | ✅ | Customers collecting board themselves | Distance-based | 4,940 |
| 10 | Processing of sold products | ✅ | External converters printing and cutting our board | Proxy: own converting energy | 24,443 |
| 11 | Use of sold products | ➖ | Cartons and plasterboard use no energy in use | Not relevant | – |
| 12 | End-of-life treatment | ✅ | Recycling, incineration, landfill of our products | Average-data, biogenic CO₂ excluded | 14,775 |
| 13-15 | Leased assets · franchises · investments | ➖ | None material | Not relevant | – |

![Scope 3 by category](assets/charts/02_scope3_categories.png)

#### How supplier data gets into Category 1

Category 1 is where **sustainable procurement** has the most influence. A supplier's own product carbon footprint replaces a generic database value, but only if its data quality is good enough:

![Animated supplier data flow](assets/animated/supplier_data_flow.svg)

**Example:** Starch Mill Central reports **0.62 kg CO₂e/kg** with DQR 1.8 ✔. That replaces the default 0.85, and Cat 1 starch emissions fall from 14,620 t to **10,664 t**. Better data, not just lower numbers: a supplier with weak data (RCP Trader Benelux, DQR 3.6) is **not** accepted until it improves.

---

### 2.5 Avoiding common mistakes

| Pitfall | How this model handles it |
|---|---|
| **Double counting internal flows** | Board sent to our own carton and gypsum plants is *not* in Cat 1, because its gas and power are already in Scope 1/2. Only third-party haulage of those transfers goes to Cat 4. |
| **Adding both Scope 2 methods** | Both are reported, but only **market-based** goes into the total. |
| **Netting biogenic carbon** | The CO₂ stored in fibre (~1,467 kg per t board) is shown as a memo item, never subtracted. |
| **Burdening recycled material twice** | Cut-off approach: recovered paper and trim carry only collection/sorting emissions, and no recycling credit is claimed at end-of-life. |
| **Silently skipping categories** | All 15 categories are screened; the 5 excluded ones are listed with a reason. |

<details>
<summary><b>Text-based flow diagrams (Mermaid)</b></summary>

#### Scope flow

```mermaid
flowchart LR
    subgraph UP["⬅ UPSTREAM · Scope 3"]
        direction TB
        RCP["Recovered paper collectors<br/>Cat 1 · Cat 4"]
        MAT["Starch · fillers · chemicals · inks<br/>Cat 1"]
        GYP["Gypsum: natural · FGD · recycled<br/>Cat 1 · Cat 4"]
        FUEL["Fuel & power production<br/>Cat 3"]
        CAP["Capex · services · travel · commuting<br/>Cat 2 · 6 · 7"]
    end
    subgraph OWN["🏭 OWN OPERATIONS · Scope 1 + 2"]
        direction TB
        MILL["Recycled board mill<br/>S1 gas · S2 electricity"]
        FC["Folding carton plants<br/>S1 · S2"]
        GB["Gypsum board plants<br/>S1 calcination & drying · S2"]
        WASTE["Rejects & wastewater<br/>Cat 5"]
        MILL -->|board| FC
        MILL -->|liner board| GB
        FC -.->|"♻ 12 % trim"| MILL
        MILL --> WASTE
    end
    subgraph DOWN["➡ DOWNSTREAM · Scope 3"]
        direction TB
        CONV["External converters<br/>Cat 9 · Cat 10"]
        RET["Brand owners & retail<br/>Cat 4 outbound · Cat 9"]
        BUILD["Construction<br/>Cat 11: no use-phase emissions"]
        EOL["End-of-life<br/>Cat 12"]
        CONV --> EOL
        RET --> EOL
        BUILD --> EOL
    end
    GRID(["Electricity grid<br/>Scope 2"])

    UP ==>|raw materials, energy, services| OWN
    GRID ==> OWN
    OWN ==>|board · cartons · gypsum board| DOWN

    classDef s1 fill:#e6f0fc,stroke:#2a78d6,color:#0b0b0b
    classDef s3 fill:#e8f7f1,stroke:#1baf7a,color:#0b0b0b
    classDef s2 fill:#fdeee7,stroke:#eb6834,color:#0b0b0b
    class MILL,FC,GB s1
    class RCP,MAT,GYP,CAP,FUEL,WASTE,CONV,RET,BUILD,EOL s3
    class GRID s2
```

#### Scope 2 methods

```mermaid
flowchart LR
    E["Electricity use<br/>232 GWh"] --> LB["Location-based<br/>× grid average 0.363 kg/kWh"]
    E --> MB["Market-based"]
    MB --> G["25 % with Guarantees of Origin / PPA<br/>× 0 kg/kWh"]
    MB --> R["75 % without certificates<br/>× residual mix 0.62 kg/kWh"]
    LB --> LBR["84,232 t CO₂e"]
    G --> MBR["107,900 t CO₂e"]
    R --> MBR
```

</details>

---

## 3. Results

![Scope split](assets/charts/01_scope_split.png)

![Scope 3 categories](assets/charts/02_scope3_categories.png)

**Key insights**

- **The Scope 3 total is driven by a few categories.** Purchased goods (Cat 1), fuel upstream (Cat 3), transport (Cat 4) and processing of sold board (Cat 10) make up about 70 % of Scope 3.
- **Recovered paper is a low-carbon raw material.** Under the cut-off approach it carries only collection and sorting emissions (~0.015 kg CO₂e/kg). The mill's energy use is the hotspot, not the fibre.
- **Supplier data matters most where factors are high.** Starch, inks and chemicals are small by mass but dominate Cat 1 emissions.

---

## 4. Product carbon footprints (LCA)

| Product | Functional unit | PCF (cradle-to-gate, fossil) | Main hotspot |
|---|---|---:|---|
| Recycled cartonboard | 1 t | **717 kg CO₂e** | Natural gas for steam & drying (48 %) |
| Folding carton | 1 t | **1,057 kg CO₂e** | Board input incl. 12 % trim (77 %) |
| Gypsum board 12.5 mm | 1 m² | **2.26 kg CO₂e** | Board drying + calcination gas (60 %) |

![PCF hotspots](assets/charts/03_pcf_hotspots.png)

```mermaid
flowchart LR
    subgraph A1["A1 · Raw materials"]
        r1["Recovered paper<br/>burden-free (cut-off)"]
        r2["Starch · CaCO₃ · chemicals"]
        r3["Inks · varnish · adhesive"]
        r4["Gypsum · glass fibre · additives"]
    end
    subgraph A2["A2 · Transport"]
        t1["Inbound t·km × HGV / rail factor"]
    end
    subgraph A3["A3 · Manufacturing"]
        m1["Board mill<br/>gas + electricity"]
        m2["Converting<br/>print · cut · glue"]
        m3["Gypsum plant<br/>calcine · form · dry"]
    end
    A1 --> A2 --> A3 --> GATE(["Factory gate = PCF"])
    m1 -->|"PCF board feeds"| m2
    m1 -->|"liner board"| m3
    BIO["Biogenic carbon stored<br/>≈ −1,467 kg CO₂ / t board<br/>(memo item, not netted)"] -.- GATE
```

---

## 5. Supplier data & sustainable procurement

### Data validation logic (PACT Pathfinder)

```mermaid
flowchart TD
    A["Purchasing sends survey + PCF request"] --> B{"Supplier PCF provided?"}
    B -- No --> S["Use secondary emission factor<br/>→ action: request PCF"]
    B -- Yes --> C["Rate 5 PACT indicators 1-5<br/>technology · geography · time · completeness · reliability"]
    C --> D{"DQR ≤ 3.0?"}
    D -- Yes --> P["✅ Use supplier-specific PCF<br/>→ annual update"]
    D -- No --> F["⚠ Use secondary factor<br/>→ action: improve primary data"]
    P --> E["Volume × applied factor = Cat 1 emissions"]
    S --> E
    F --> E
    E --> K["KPI: share of Cat 1 from supplier-specific data"]
```

![Supplier data coverage](assets/charts/06_supplier_data_coverage.png)

### ESG scorecard

Score = 30 % Environment + 20 % Labour & Human Rights + 15 % Ethics + 10 % Sustainable Procurement + 25 % Climate maturity. Climate maturity combines SBTi target, accepted PCF, ISO 14001 and ISO 50001.

| Rating | Score | Action |
|---|---|---|
| **A** – Strategic partner | ≥ 70 | Joint decarbonisation roadmap, PCF exchange |
| **B** – Develop | ≥ 55 | Request EcoVadis + SBTi commitment |
| **C** – Improvement plan | ≥ 40 | Corrective action plan within 6 months |
| **D** – Escalate | < 40 | Escalate to category management, audit |

![Supplier scorecard](assets/charts/05_supplier_scorecard.png)

---

## 6. Decarbonisation levers

Ten levers identify **~142,000 t CO₂e/yr (≈ 28 %)** of reduction potential. The abatement cost is (capex ÷ lifetime + Δ opex) ÷ annual reduction.

![MACC](assets/charts/04_macc.png)

| ID | Lever | Scope | t CO₂e/yr | EUR/t |
|---|---|---|---:|---:|
| L09 | Board lightweighting in folding cartons (−5 % grammage) | Mixed | 4,276 | −246 |
| L04 | Heat recovery in gypsum board dryers | S1 | 7,272 | −41 |
| L01 | Additional renewable PPA (+50 % of electricity) | S2 | 71,933 | 25 |
| L02 | Heat pumps / MVR for board drying steam | S1 | 27,153 | 37 |
| L10 | Electric collection trucks at RCP suppliers | S3 | 1,845 | 54 |
| L06 | Low-carbon starch (supplier engagement) | S3 | 3,199 | 78 |
| L03 | Electrode boiler on renewable power | S1 | 20,365 | 103 |
| L07 | Low-carbon / bio-based inks | S3 | 1,063 | 141 |
| L08 | Modal shift of RCP inbound to rail | S3 | 1,779 | 169 |
| L05 | Biomethane for gypsum calcination | S1 | 3,386 | 487 |

---

## 7. How the model works

```mermaid
flowchart LR
    CI["Company_Inputs<br/>production volumes"] --> PCF
    EF["Emission_Factors<br/>32 factors + sources"] --> PCF["PCF_Board → PCF_FoldingCarton<br/>PCF_Board → PCF_GypsumBoard"]
    EF --> SR["Supplier_Register<br/>volumes · PCFs · DQR"]
    PCF --> GHG["GHG_Inventory<br/>Scope 1 · 2 · 3"]
    CI --> GHG
    SR --> GHG
    SR --> SC["Supplier_Scorecard<br/>ESG rating A-D"]
    GHG --> DEC["Decarbonisation<br/>levers · MACC"]
    GHG & SC & DEC & PCF --> KPI["KPI_Dashboard"]
    SV["Supplier_Survey"] -.-> SR & SC
```

- **Every result is a formula** (711 formulas, zero errors). Change any blue input cell and the whole model updates.
- **Built-in checks.** Mass balances reconcile recovered paper and gypsum in the supplier register against what production needs (deviation ≤ 2 %).
- **Colour code.** Blue on yellow = input, black = formula, green = link to another sheet.

---

## 8. Repository structure & how to run

```
Cardboad-example/
├── model/LCA_CO2_Supplier_Toolkit.xlsx   # the Excel model (13 sheets)
├── docs/index.html                        # interactive dashboard (GitHub Pages)
├── docs/methodology.md                    # standards, boundaries, assumptions
├── assets/                                # diagrams, chart PNGs, screenshots
├── data/                                  # CSV/JSON exports of model results
├── src/
│   ├── build_workbook.py                  # generates the Excel model
│   ├── export_data.py                     # workbook → CSV/JSON
│   ├── make_charts.py                     # JSON → PNG charts
│   ├── dashboard_template.html            # dashboard source
│   └── build_dashboard.py                 # JSON → docs/index.html
└── requirements.txt
```

```bash
pip install -r requirements.txt
python src/build_workbook.py      # 1. build the Excel model
# 2. open the workbook in Excel and save it once (or run a LibreOffice recalc) so the formula values are calculated
python src/export_data.py         # 3. export results
python src/make_charts.py         # 4. README charts
python src/build_dashboard.py     # 5. dashboard
```

---

## 9. Methodology & limitations

See [`docs/methodology.md`](docs/methodology.md) for details. In short:

- **Standards:** ISO 14040/44, ISO 14067, GHG Protocol Corporate, Scope 2 & Scope 3 Standards, GHG Protocol Product Standard, PACT Pathfinder v3, CEPI Carbon Footprint Framework, EN 15804.
- **Boundary:** cradle-to-gate (A1-A3), GWP100 (IPCC AR6), fossil GHG only. Biogenic carbon is reported separately.
- **Recycling allocation:** cut-off (recycled-content) approach. Recovered paper and trim carry no burden from their first life.

> ⚠️ **Disclaimer:** the company, suppliers and all figures are **fictional**. Emission factors are rounded, indicative values typical of public sources (UBA, DESNZ, AIB, ecoinvent-type averages). They are not verified and must be replaced with licensed data before any real reporting (CSRD/ESRS E1, customer PCF requests, EcoVadis).

## License

MIT. See [LICENSE](LICENSE).
