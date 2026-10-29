# Methodology

## 1. Standards

| Topic | Standard / framework |
|---|---|
| LCA framework | ISO 14040 / ISO 14044 |
| Product Carbon Footprint | ISO 14067:2018, GHG Protocol Product Standard |
| Sector guidance | CEPI Carbon Footprint Framework for paper & board, EN 15804+A2 (gypsum board, modules A1-A3) |
| Corporate inventory | GHG Protocol Corporate Standard, Scope 2 Guidance, Corporate Value Chain (Scope 3) Standard |
| Supplier PCF exchange & data quality | WBCSD PACT Pathfinder Framework v3 |
| Supplier ESG assessment | EcoVadis themes (Environment, Labour & Human Rights, Ethics, Sustainable Procurement) |
| Characterisation | GWP100, IPCC AR6 |

## 2. Product carbon footprints

| | Board | Folding carton | Gypsum board |
|---|---|---|---|
| Declared / functional unit | 1 t recycled cartonboard | 1 t printed folding cartons | 1 m² plasterboard 12.5 mm (~8.5 kg) |
| Boundary | Cradle-to-gate | Cradle-to-gate (+ optional distribution) | A1-A3 |
| Key primary data | Mill gas & power metering, RCP yield 1.15 t/t | Board input 1.136 t/t (12 % trim), inks, energy | Recipe (9 t gypsum, 0.4 t liner per 1,000 m²), calcination & drying gas |
| Link | – | Board PCF from `PCF_Board` | Liner PCF from `PCF_Board` |

**Recycling allocation: cut-off.** Recovered paper and internal trim enter burden-free. Only collection, sorting and baling (EF08) are allocated. Under cut-off, the end-of-life recycling of our products gives no credit either, so nothing is double counted.

**Biogenic carbon** stored in the fibre (0.40 kg C/kg → about 1,467 kg CO₂ per t board) is shown as a memo item, as ISO 14067 requires. It is not netted against fossil emissions.

## 3. Corporate inventory

- **Organisational boundary:** operational control.
- **Scope 1:** natural gas (board mills, converting plants, gypsum calcination and drying) and diesel for mobile equipment.
- **Scope 2:** location-based (UBA grid mix) and market-based (Guarantees of Origin / PPA at 0, the rest at the AIB residual mix). The total uses market-based.
- **Scope 3:** all 15 categories are screened. Categories 8, 11, 13, 14 and 15 are excluded with a justification.
- **Internal flows** (board to own converting and gypsum plants) are not counted as Cat 1. Their energy is already in Scope 1/2, which avoids double counting. Third-party haulage of internal transfers is counted in Cat 4.

## 4. Supplier data quality (PACT DQR)

Each supplier PCF is rated on five indicators from 1 (very good) to 5 (very poor):

| Indicator | Question |
|---|---|
| TeR, technological representativeness | Does the data reflect the actual product and process? |
| GeR, geographical representativeness | Is it the supplying site or country? |
| TiR, temporal representativeness | Is the data ≤ 2 years old? |
| Completeness | Are all relevant processes and sites covered? |
| Reliability | Is it measured or verified, rather than estimated? |

DQR is the average of the five. **Acceptance rule:** use the supplier PCF if DQR ≤ 3.0; otherwise use the secondary factor and give the supplier an improvement action. The threshold is an input cell.

## 5. Supplier scorecard

`Total = Σ (theme score × weight)`. Default weights: 30 % Environment, 20 % Labour & HR, 15 % Ethics, 10 % Sustainable Procurement, 25 % Climate maturity.
Climate maturity = 40 points SBTi target + 30 points accepted PCF + 15 points ISO 14001 + 15 points ISO 50001.
Risk index = supplier's share of Cat 1 emissions × (100 − score). Engage the highest values first.

## 6. Decarbonisation

Abatement cost (EUR/t) = (capex ÷ lifetime + Δ annual opex) ÷ annual reduction. There is no discounting. Levers are compared against a reference CO₂ price (input, default 100 EUR/t). L02 and L03 both act on board-mill gas, so they are not fully additive.

## 7. Emission factors

32 factors are listed with their source in the `Emission_Factors` sheet. They are **indicative, rounded values** in the style of UBA, DESNZ 2024, AIB and ecoinvent-type averages, for demonstration only. Replace them with licensed or verified data before any external use.

## 8. Limitations

- All company and supplier data is fictional.
- Proxies are used where data is missing (process chemicals, additives, Cat 10 processing).
- Spend-based factors (Cat 1 indirect, Cat 2) carry high uncertainty and should be replaced step by step with supplier-specific data.
- No uncertainty analysis has been done yet. A Monte Carlo analysis is a possible extension.
