
Ansvarsområden:
1.Data & EDA (target-fördelning, missing values, 2 figurer + insikter) Milda
2.Pipeline & preprocessing (leakage-säker, hantering av numeriskt/kategoriskt, reproducibility) Elias
3.Modelljämförelse (baseline + minst 2 modeller, CV-upplägg) Azar
4.Optimering (tuning av 1 vald modell, 1–2 parametrar) Ben
5.Threshold/prioritering (koppla kravkort → metric + FP/FN-konsekvens) Ida
6.Pitch & risker (presentation, rekommendation, begränsningar, nästa steg) Emmad
Krav: I presentationen ska det framgå vem som ansvarade för vad (en rad per person).

## Hur man kör programent
1. Klona projektet:
git clone https://github.com/eliasstalfreelancer/GruppArbete_ML_Grupp_6.git
2. Gå till mappen:
cd GruppArbete_ML_Grupp_6
3. Installera beroenden:
pip install -r requirements.txt
4. Kör projektet:
jupyter notebook report.ipynb

## Kravkort
Stakeholder: Trust & Safety
Prioritet: Hög recall och minimera False Negatives (FN). Det viktigaste är att inte missa farliga fall.

## Strategi
Vi använder en Top-X-prioritering där de X% fall med högst risk-score flaggas för granskning. Detta gör att de mest riskabla fallen prioriteras. Strategin är anpassad för att maximera recall och minska risken för missade farliga fall, även om det leder till fler False Positives. Vi testade flera värden på X och valde det som bäst matchade kravet på hög recall och låg andel missade fall.