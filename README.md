Om gruppen har färre personer än områden: slå ihop områden och gör vissa delar tillsammans.
Ansvarsområden:
1.Data & EDA (target-fördelning, missing values, 2 figurer + insikter) Milda
2.Pipeline & preprocessing (leakage-säker, hantering av numeriskt/kategoriskt, reproducibility) Elias
3.Modelljämförelse (baseline + minst 2 modeller, CV-upplägg) Azar
4.Optimering (tuning av 1 vald modell, 1–2 parametrar) Ben
5.Threshold/prioritering (koppla kravkort → metric + FP/FN-konsekvens)
6.Pitch & risker (presentation, rekommendation, begränsningar, nästa steg)
Krav: I presentationen ska det framgå vem som ansvarade för vad (en rad per person).




## Kravkort
Stakeholder: Trust  Safety
Prioritet: Hög recall och minimera False Negatives (FN). Det viktigast är att inte missa farliga fall.

## Strategi: Top-50
Vi flaggar de 50 fall med högst risk-score. Top-X strategin ökar chansen att fånga de mest riskabla fallen och minskar risken för att farliga fall missas, även om det innebär fler False Positives (FP).