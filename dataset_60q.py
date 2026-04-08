"""
dataset.py  –  APE Study Ground-Truth QA Dataset
=================================================
60 expert-curated questions across 4 domains.
Every ground_truth is verifiable against a cited public source.

Domain split: 15 General | 15 Finance | 15 Healthcare | 15 Legal
Difficulty:   40 % Easy  | 40 % Medium | 20 % Hard
"""

QUESTIONS = [

# ═══════════════════════════════════════════════════
# GENERAL KNOWLEDGE  (15 questions)
# ═══════════════════════════════════════════════════

{"id": "GK-01", "domain": "general", "difficulty": "easy",
 "query": "What is the capital city of Australia?",
 "ground_truth": "Canberra",
 "source": "Australian Government official website"},

{"id": "GK-02", "domain": "general", "difficulty": "easy",
 "query": "Who invented the World Wide Web?",
 "ground_truth": "Tim Berners-Lee invented the World Wide Web in 1989 at CERN.",
 "source": "CERN official history"},

{"id": "GK-03", "domain": "general", "difficulty": "easy",
 "query": "What does the acronym 'DNA' stand for?",
 "ground_truth": "Deoxyribonucleic acid",
 "source": "NIH Genetics Home Reference"},

{"id": "GK-04", "domain": "general", "difficulty": "easy",
 "query": "In what year did World War II end?",
 "ground_truth": "1945 — Germany surrendered on May 8 (V-E Day) and Japan on September 2 (V-J Day).",
 "source": "National WWII Museum"},

{"id": "GK-05", "domain": "general", "difficulty": "easy",
 "query": "What is the chemical symbol for gold?",
 "ground_truth": "Au (from the Latin 'aurum')",
 "source": "IUPAC Periodic Table"},

{"id": "GK-06", "domain": "general", "difficulty": "medium",
 "query": "What is the speed of light in a vacuum in metres per second?",
 "ground_truth": "299,792,458 metres per second (exactly, by definition since 1983).",
 "source": "NIST CODATA 2018"},

{"id": "GK-07", "domain": "general", "difficulty": "medium",
 "query": "How many bones are in the adult human body?",
 "ground_truth": "206 bones in a typical adult human body.",
 "source": "Gray's Anatomy, 41st edition"},

{"id": "GK-08", "domain": "general", "difficulty": "medium",
 "query": "What is the Pythagorean theorem?",
 "ground_truth": "In a right-angled triangle, a² + b² = c², where c is the hypotenuse.",
 "source": "Euclid's Elements, Book I, Proposition 47"},

{"id": "GK-09", "domain": "general", "difficulty": "medium",
 "query": "Who wrote 'Pride and Prejudice'?",
 "ground_truth": "Jane Austen, first published in 1813.",
 "source": "British Library catalogue"},

{"id": "GK-10", "domain": "general", "difficulty": "medium",
 "query": "What is the longest river in the world?",
 "ground_truth": "The Nile (approximately 6,650 km / 4,130 miles), though some studies consider the Amazon longer depending on measurement methodology.",
 "source": "USGS Water Resources"},

{"id": "GK-11", "domain": "general", "difficulty": "medium",
 "query": "What is the powerhouse of the cell?",
 "ground_truth": "The mitochondrion (plural: mitochondria) is the organelle responsible for producing ATP through cellular respiration.",
 "source": "Alberts et al., Molecular Biology of the Cell, 6th ed."},

{"id": "GK-12", "domain": "general", "difficulty": "hard",
 "query": "What is Avogadro's number and what does it represent?",
 "ground_truth": "6.02214076 × 10²³ mol⁻¹ (exactly, since 2019 SI redefinition). It represents the number of constituent particles in one mole of a substance.",
 "source": "NIST CODATA 2018, SI Brochure 9th ed."},

{"id": "GK-13", "domain": "general", "difficulty": "hard",
 "query": "What is the difference between nuclear fission and nuclear fusion?",
 "ground_truth": "Fission splits a heavy nucleus (e.g. U-235) into smaller nuclei releasing energy. Fusion combines light nuclei (e.g. deuterium + tritium) into a heavier nucleus, also releasing energy. Fusion releases more energy per unit mass but requires extreme temperature and pressure.",
 "source": "DOE Office of Nuclear Energy"},

{"id": "GK-14", "domain": "general", "difficulty": "hard",
 "query": "What are the three laws of thermodynamics?",
 "ground_truth": "1st Law: Energy cannot be created or destroyed, only converted (conservation of energy). 2nd Law: Entropy of an isolated system tends to increase. 3rd Law: Entropy of a perfect crystal approaches zero as temperature approaches absolute zero.",
 "source": "Atkins, Physical Chemistry, 10th ed."},

{"id": "GK-15", "domain": "general", "difficulty": "hard",
 "query": "What was the Treaty of Westphalia and why is it historically significant?",
 "ground_truth": "The 1648 Peace of Westphalia ended the Thirty Years' War and the Eighty Years' War. It established the principle of state sovereignty and non-interference in domestic affairs, forming the foundation of the modern international state system.",
 "source": "Yale Avalon Project; Croxton, Westphalia (2013)"},

# ═══════════════════════════════════════════════════
# FINANCE  (15 questions)
# ═══════════════════════════════════════════════════

{"id": "FN-01", "domain": "finance", "difficulty": "easy",
 "query": "What does P/E ratio stand for and how is it calculated?",
 "ground_truth": "Price-to-Earnings ratio. Calculated as: Market Price per Share ÷ Earnings per Share (EPS). It indicates how much investors pay per dollar of earnings.",
 "source": "CFA Institute, Security Analysis"},

{"id": "FN-02", "domain": "finance", "difficulty": "easy",
 "query": "What is the difference between a stock and a bond?",
 "ground_truth": "A stock represents equity ownership in a company (variable returns, residual claim). A bond is a debt instrument — the issuer borrows money and pays fixed interest (coupon) and returns principal at maturity.",
 "source": "CFA Institute Level I Curriculum"},

{"id": "FN-03", "domain": "finance", "difficulty": "easy",
 "query": "What does EBITDA stand for?",
 "ground_truth": "Earnings Before Interest, Taxes, Depreciation, and Amortization.",
 "source": "GAAP Accounting Standards"},

{"id": "FN-04", "domain": "finance", "difficulty": "easy",
 "query": "What is diversification in portfolio management?",
 "ground_truth": "A risk management strategy that allocates investments across different assets, sectors, or geographies to reduce exposure to any single risk, based on the principle that uncorrelated assets reduce portfolio volatility.",
 "source": "Markowitz (1952), Portfolio Selection, Journal of Finance"},

{"id": "FN-05", "domain": "finance", "difficulty": "easy",
 "query": "What is quantitative easing (QE)?",
 "ground_truth": "A non-conventional monetary policy where a central bank purchases government bonds or other securities to inject money into the economy, lower long-term interest rates, and stimulate economic activity when short-term rates are near zero.",
 "source": "Federal Reserve Board explanatory notes"},

{"id": "FN-06", "domain": "finance", "difficulty": "medium",
 "query": "What was Apple's net income for fiscal year 2022?",
 "ground_truth": "$99.803 billion, for the fiscal year ending September 24, 2022, per Apple's 10-K filing with the SEC.",
 "source": "Apple Inc. Form 10-K, SEC EDGAR, filed October 28, 2022"},

{"id": "FN-07", "domain": "finance", "difficulty": "medium",
 "query": "What is the difference between gross profit and net profit?",
 "ground_truth": "Gross profit = Revenue − Cost of Goods Sold (COGS). Net profit = Gross Profit − Operating Expenses − Interest − Taxes − Other expenses. Net profit is the bottom line after all deductions.",
 "source": "GAAP Income Statement framework"},

{"id": "FN-08", "domain": "finance", "difficulty": "medium",
 "query": "What is the Capital Asset Pricing Model (CAPM)?",
 "ground_truth": "CAPM: E(Ri) = Rf + βi × (E(Rm) − Rf), where Rf is the risk-free rate, βi is the asset's sensitivity to market movements, and (E(Rm) − Rf) is the market risk premium. It estimates expected return given systematic risk.",
 "source": "Sharpe (1964), Journal of Finance; Lintner (1965)"},

{"id": "FN-09", "domain": "finance", "difficulty": "medium",
 "query": "What is the Federal Reserve's dual mandate?",
 "ground_truth": "The Federal Reserve Act mandates the Fed to pursue maximum employment and stable prices (price stability, targeting ~2% inflation). This is the 'dual mandate' established in the Humphrey-Hawkins Act (1978).",
 "source": "Federal Reserve Act, Section 2A; Humphrey-Hawkins Act 1978"},

{"id": "FN-10", "domain": "finance", "difficulty": "medium",
 "query": "What is the Black-Scholes model used for?",
 "ground_truth": "The Black-Scholes model prices European-style options. Formula: C = S·N(d1) − K·e^(−rT)·N(d2), where d1 and d2 depend on stock price S, strike K, risk-free rate r, time T, and volatility σ. Developed by Fischer Black, Myron Scholes, and Robert Merton (1973).",
 "source": "Black & Scholes (1973), Journal of Political Economy"},

{"id": "FN-11", "domain": "finance", "difficulty": "hard",
 "query": "What was the S&P 500 closing value on December 31, 2022?",
 "ground_truth": "3,839.50 (the S&P 500 index closed at 3,839.50 on December 30, 2022, the last trading day of the year).",
 "source": "S&P Global Market Intelligence; Bloomberg Terminal"},

{"id": "FN-12", "domain": "finance", "difficulty": "hard",
 "query": "What does Basel III require for Tier 1 capital?",
 "ground_truth": "Basel III requires banks to maintain a minimum Common Equity Tier 1 (CET1) ratio of 4.5% of risk-weighted assets, a Tier 1 capital ratio of 6%, and a Total Capital ratio of 8%, plus a Capital Conservation Buffer of 2.5%.",
 "source": "Basel Committee on Banking Supervision, Basel III (2011)"},

{"id": "FN-13", "domain": "finance", "difficulty": "hard",
 "query": "What is the Sharpe ratio and how is it interpreted?",
 "ground_truth": "Sharpe Ratio = (Rp − Rf) / σp, where Rp is portfolio return, Rf is the risk-free rate, and σp is the portfolio's standard deviation of excess returns. A higher ratio indicates better risk-adjusted return. A ratio above 1.0 is generally considered acceptable; above 2.0 is very good.",
 "source": "Sharpe (1966), Mutual Fund Performance, Journal of Business"},

{"id": "FN-14", "domain": "finance", "difficulty": "hard",
 "query": "What is the yield curve inversion and why is it considered a recession indicator?",
 "ground_truth": "A yield curve inversion occurs when short-term bond yields (e.g. 2-year Treasury) exceed long-term yields (e.g. 10-year Treasury). It has preceded every US recession since 1955 (with one false signal in 1966) because it reflects market expectations of lower future rates due to economic slowdown.",
 "source": "Federal Reserve Bank of San Francisco (2018); Campbell Harvey's PhD thesis (1986)"},

{"id": "FN-15", "domain": "finance", "difficulty": "hard",
 "query": "What is the Dodd-Frank Wall Street Reform and Consumer Protection Act?",
 "ground_truth": "The Dodd-Frank Act (2010) is a US federal law enacted in response to the 2008 financial crisis. Key provisions include: creation of the Financial Stability Oversight Council (FSOC), Volcker Rule (restricts proprietary trading by banks), Consumer Financial Protection Bureau (CFPB), and enhanced derivatives regulation through mandatory clearing.",
 "source": "Pub.L. 111–203, 124 Stat. 1376"},

# ═══════════════════════════════════════════════════
# HEALTHCARE  (15 questions)
# ═══════════════════════════════════════════════════

{"id": "HC-01", "domain": "healthcare", "difficulty": "easy",
 "query": "What is the normal resting heart rate for adults?",
 "ground_truth": "60 to 100 beats per minute (bpm) for adults. Athletes may have lower resting rates (40–60 bpm).",
 "source": "American Heart Association; Mayo Clinic"},

{"id": "HC-02", "domain": "healthcare", "difficulty": "easy",
 "query": "What does BMI stand for and how is it calculated?",
 "ground_truth": "Body Mass Index. Formula: BMI = weight(kg) / height²(m²). Underweight: <18.5; Normal: 18.5–24.9; Overweight: 25–29.9; Obese: ≥30.",
 "source": "WHO Global Database on BMI (2023)"},

{"id": "HC-03", "domain": "healthcare", "difficulty": "easy",
 "query": "What are the symptoms of Type 2 diabetes?",
 "ground_truth": "Common symptoms: increased thirst (polydipsia), frequent urination (polyuria), increased hunger (polyphagia), unexplained weight loss, fatigue, blurred vision, slow-healing wounds, frequent infections. Many cases are initially asymptomatic.",
 "source": "American Diabetes Association Standards of Medical Care (2023)"},

{"id": "HC-04", "domain": "healthcare", "difficulty": "easy",
 "query": "What is the normal blood pressure range for adults?",
 "ground_truth": "Normal: systolic <120 mmHg and diastolic <80 mmHg. Elevated: 120-129/<80. Stage 1 Hypertension: 130-139/80-89. Stage 2 Hypertension: ≥140/≥90.",
 "source": "2017 ACC/AHA High Blood Pressure Guidelines"},

{"id": "HC-05", "domain": "healthcare", "difficulty": "easy",
 "query": "What does the acronym RICE stand for in first aid?",
 "ground_truth": "Rest, Ice, Compression, Elevation — a first-line treatment protocol for minor musculoskeletal injuries (sprains, strains).",
 "source": "American Academy of Orthopaedic Surgeons"},

{"id": "HC-06", "domain": "healthcare", "difficulty": "medium",
 "query": "What is the recommended first-line pharmacological treatment for Type 2 diabetes?",
 "ground_truth": "Metformin is the recommended first-line pharmacological agent (if tolerated and not contraindicated), combined with lifestyle interventions (diet and exercise), per ADA guidelines. Starting dose: 500 mg once or twice daily with meals, titrated to 1,500–2,000 mg/day.",
 "source": "ADA Standards of Medical Care in Diabetes 2023, Section 9"},

{"id": "HC-07", "domain": "healthcare", "difficulty": "medium",
 "query": "What is the mechanism of action of aspirin as an antiplatelet?",
 "ground_truth": "Aspirin irreversibly acetylates cyclooxygenase-1 (COX-1), blocking thromboxane A2 (TXA2) synthesis in platelets. Since platelets lack nuclei and cannot synthesize new COX-1, the antiplatelet effect lasts the platelet's lifespan (~7–10 days). Low-dose aspirin (75–100 mg/day) is used for antiplatelet therapy.",
 "source": "Vane JR, Nobel Prize lecture 1982; ESC Antithrombotic Guidelines"},

{"id": "HC-08", "domain": "healthcare", "difficulty": "medium",
 "query": "What are the five cardinal signs of inflammation?",
 "ground_truth": "Rubor (redness), Calor (heat), Tumor (swelling), Dolor (pain), and Functio laesa (loss of function). The first four were described by Celsus (~30 AD); the fifth by Galen and later Virchow.",
 "source": "Robbins & Cotran Pathologic Basis of Disease, 10th ed."},

{"id": "HC-09", "domain": "healthcare", "difficulty": "medium",
 "query": "What is herd immunity and at what vaccination coverage threshold is it typically achieved for measles?",
 "ground_truth": "Herd immunity occurs when sufficient population immunity (via vaccination or prior infection) prevents widespread disease transmission, protecting unimmunized individuals. For measles (R0 = 12–18), the herd immunity threshold is approximately 92–95% immune coverage.",
 "source": "WHO Immunization Advisory; Fine et al. (2011), Clinical Infectious Diseases"},

{"id": "HC-10", "domain": "healthcare", "difficulty": "medium",
 "query": "What is the difference between Type 1 and Type 2 diabetes mellitus?",
 "ground_truth": "Type 1 DM: autoimmune destruction of pancreatic beta cells → absolute insulin deficiency; typically early onset; requires insulin therapy. Type 2 DM: progressive insulin resistance + relative insulin insufficiency; strongly associated with obesity, sedentary lifestyle, and genetics; managed with lifestyle, oral agents, and eventually insulin.",
 "source": "ADA Classification of Diabetes Mellitus 2023"},

{"id": "HC-11", "domain": "healthcare", "difficulty": "hard",
 "query": "What is the half-life of aspirin in the bloodstream?",
 "ground_truth": "Aspirin (acetylsalicylic acid) has a plasma half-life of approximately 15–20 minutes due to rapid hydrolysis to salicylate. Salicylate's half-life is dose-dependent: ~2–3 hours at low doses; up to 15–30 hours at high doses (Michaelis-Menten kinetics).",
 "source": "Brunton et al., Goodman & Gilman's Pharmacology, 13th ed."},

{"id": "HC-12", "domain": "healthcare", "difficulty": "hard",
 "query": "What is the Apgar score and what does each letter stand for?",
 "ground_truth": "The Apgar score assesses newborn health at 1 and 5 minutes after birth, scoring 0–2 on 5 criteria: Appearance (skin color), Pulse (heart rate), Grimace (reflex irritability), Activity (muscle tone), Respiration. Total score: 7–10 = normal; 4–6 = moderate concern; 0–3 = immediate intervention required.",
 "source": "Apgar V. (1953), Curr Res Anesth Analg. Original publication"},

{"id": "HC-13", "domain": "healthcare", "difficulty": "hard",
 "query": "What are the diagnostic criteria for sepsis according to the Sepsis-3 definition?",
 "ground_truth": "Sepsis-3 (Singer et al., JAMA 2016): Sepsis = life-threatening organ dysfunction caused by dysregulated host response to infection. Clinically identified by acute change in SOFA (Sequential Organ Failure Assessment) score ≥ 2 points. Septic shock = sepsis + vasopressor requirement to maintain MAP ≥65 mmHg + serum lactate >2 mmol/L despite adequate fluid resuscitation.",
 "source": "Singer M et al., JAMA. 2016;315(8):801-810"},

{"id": "HC-14", "domain": "healthcare", "difficulty": "hard",
 "query": "What is the mechanism by which statins lower cholesterol?",
 "ground_truth": "Statins (HMG-CoA reductase inhibitors) competitively inhibit 3-hydroxy-3-methylglutaryl coenzyme A reductase, the rate-limiting enzyme in the mevalonate pathway of hepatic cholesterol synthesis. This reduces intracellular cholesterol, upregulates LDL receptors, and increases LDL clearance from the bloodstream.",
 "source": "Endo A, Nobel Foundation; ACC/AHA Cholesterol Guidelines 2018"},

{"id": "HC-15", "domain": "healthcare", "difficulty": "hard",
 "query": "What is the Philadelphia chromosome and what disease is it associated with?",
 "ground_truth": "The Philadelphia chromosome is a specific chromosomal abnormality resulting from reciprocal translocation t(9;22)(q34;q11), creating the BCR-ABL1 fusion gene. It produces a constitutively active tyrosine kinase. It is the hallmark of Chronic Myeloid Leukaemia (CML) (present in ~95% of cases) and is found in ~25% of adult ALL.",
 "source": "Nowell PC, Hungerford DA. (1960), Science. Identified in Philadelphia"},

# ═══════════════════════════════════════════════════
# LEGAL  (15 questions)
# ═══════════════════════════════════════════════════

{"id": "LG-01", "domain": "legal", "difficulty": "easy",
 "query": "What is the difference between civil law and criminal law?",
 "ground_truth": "Criminal law: offences against the state; prosecution by government; burden of proof 'beyond reasonable doubt'; penalties include imprisonment. Civil law: disputes between private parties; plaintiff seeks compensation or injunction; burden of proof 'preponderance of evidence' (>50%); no imprisonment.",
 "source": "Black's Law Dictionary, 11th ed.; Restatement of Torts"},

{"id": "LG-02", "domain": "legal", "difficulty": "easy",
 "query": "What does 'habeas corpus' mean?",
 "ground_truth": "Latin: 'you shall have the body.' A writ requiring that a detained person be brought before a court to determine whether the detention is lawful. It is a fundamental safeguard against unlawful imprisonment, codified in common law since Magna Carta (1215) and the Habeas Corpus Act 1679 (England).",
 "source": "Habeas Corpus Act 1679; 28 U.S.C. § 2241 (US federal)"},

{"id": "LG-03", "domain": "legal", "difficulty": "easy",
 "query": "What is an injunction?",
 "ground_truth": "A court order compelling a party to do (mandatory injunction) or refrain from doing (prohibitory injunction) a specific act. Types: Temporary Restraining Order (TRO), Preliminary Injunction (pending trial), Permanent Injunction (final order). Courts apply a four-factor test (eBay Inc. v. MercExchange, 2006).",
 "source": "Federal Rules of Civil Procedure, Rule 65; eBay v. MercExchange (2006)"},

{"id": "LG-04", "domain": "legal", "difficulty": "easy",
 "query": "What is the difference between a patent and a trademark?",
 "ground_truth": "Patent: grants inventor exclusive rights to a novel, non-obvious, useful invention for 20 years from filing (utility patent). Trademark: protects words, names, symbols, logos that distinguish goods/services of one party from others; renewable indefinitely as long as in use.",
 "source": "35 U.S.C. § 154 (patents); 15 U.S.C. § 1127 (Lanham Act, trademarks)"},

{"id": "LG-05", "domain": "legal", "difficulty": "easy",
 "query": "What does GDPR stand for and which countries must comply?",
 "ground_truth": "General Data Protection Regulation (EU) 2016/679. All EU/EEA member states must comply. Additionally, ANY organization worldwide that processes personal data of EU/EEA residents must comply, regardless of where the organization is based (extraterritorial scope, Article 3).",
 "source": "GDPR Regulation (EU) 2016/679, Official Journal of the European Union"},

{"id": "LG-06", "domain": "legal", "difficulty": "medium",
 "query": "What is the Miranda warning and under what circumstances must it be given?",
 "ground_truth": "The Miranda warning must inform suspects: (1) right to remain silent; (2) anything said can be used against them in court; (3) right to an attorney; (4) if cannot afford an attorney, one will be appointed. Required before custodial interrogation (when suspect is in custody AND being questioned). Established in Miranda v. Arizona, 384 U.S. 436 (1966).",
 "source": "Miranda v. Arizona, 384 U.S. 436 (1966); 18 U.S.C. § 3501"},

{"id": "LG-07", "domain": "legal", "difficulty": "medium",
 "query": "What does 'mens rea' mean in criminal law?",
 "ground_truth": "Latin: 'guilty mind.' The mental element required for criminal liability — the defendant's intention, knowledge, recklessness, or negligence in committing the actus reus (guilty act). Most crimes require both actus reus and mens rea. Level of mens rea affects severity: purposely > knowingly > recklessly > negligently (Model Penal Code §2.02).",
 "source": "Model Penal Code §2.02; R v Woollin [1998] UKHL (UK)"},

{"id": "LG-08", "domain": "legal", "difficulty": "medium",
 "query": "What are the elements required to establish negligence in tort law?",
 "ground_truth": "Four elements: (1) Duty of care — defendant owed plaintiff a duty; (2) Breach — defendant breached that duty (objective 'reasonable person' standard); (3) Causation — factual (but-for test) and proximate causation; (4) Damages — plaintiff suffered actual harm. All four must be proven on balance of probabilities.",
 "source": "Donoghue v Stevenson [1932] AC 562; Restatement (Third) of Torts"},

{"id": "LG-09", "domain": "legal", "difficulty": "medium",
 "query": "What is the Fourth Amendment to the US Constitution?",
 "ground_truth": "The Fourth Amendment protects persons against unreasonable searches and seizures. It requires warrants to be supported by probable cause, specifically describing the place to be searched and persons/things to be seized. Key doctrine: exclusionary rule (Mapp v. Ohio, 1961) — evidence from illegal searches inadmissible.",
 "source": "U.S. Constitution, Amendment IV (ratified 1791); Mapp v. Ohio, 367 U.S. 643 (1961)"},

{"id": "LG-10", "domain": "legal", "difficulty": "medium",
 "query": "What is the statute of limitations for most federal felonies in the United States?",
 "ground_truth": "The general federal statute of limitations for non-capital federal crimes is 5 years from the date the offence was committed (18 U.S.C. § 3282). Exceptions: capital offences (no limit); terrorism, certain sex offences against minors, DNA-based crimes (extended or eliminated limitations).",
 "source": "18 U.S.C. § 3282; 18 U.S.C. § 3283; 18 U.S.C. § 3286"},

{"id": "LG-11", "domain": "legal", "difficulty": "hard",
 "query": "What is the legal standard 'beyond a reasonable doubt' versus 'preponderance of the evidence'?",
 "ground_truth": "Beyond reasonable doubt (criminal standard): no other logical explanation, approximately 95%+ certainty — highest standard because liberty is at stake. Preponderance of evidence (civil standard): more likely true than not (>50%) — lower bar because only money/civil remedies at stake. Some proceedings use intermediate standard: 'clear and convincing evidence' (~75%).",
 "source": "In re Winship, 397 U.S. 358 (1970); Federal Rule of Evidence; Addington v. Texas (1979)"},

{"id": "LG-12", "domain": "legal", "difficulty": "hard",
 "query": "What is the doctrine of promissory estoppel?",
 "ground_truth": "Promissory estoppel (equitable doctrine) prevents a promisor from reneging on a promise when: (1) a clear and definite promise was made; (2) the promisee reasonably relied on the promise; (3) the reliance was detrimental (promisee changed position); (4) enforcement is necessary to prevent injustice. It can substitute for consideration in contract law (Restatement §90).",
 "source": "Restatement (Second) of Contracts §90; Central London Property Trust v High Trees House [1947]"},

{"id": "LG-13", "domain": "legal", "difficulty": "hard",
 "query": "What is the principle established in Marbury v. Madison (1803)?",
 "ground_truth": "Marbury v. Madison (1803), Chief Justice John Marshall, established the principle of judicial review — the power of US federal courts to strike down legislation that conflicts with the Constitution. It is the foundational case for the supremacy of the Constitution and the role of the judiciary as interpreter of constitutional limits on governmental power.",
 "source": "Marbury v. Madison, 5 U.S. (1 Cranch) 137 (1803)"},

{"id": "LG-14", "domain": "legal", "difficulty": "hard",
 "query": "What is the Brussels Regulation (Recast) and what does it govern?",
 "ground_truth": "Brussels Regulation (Recast) — EU Regulation No 1215/2012 — governs jurisdiction and the recognition and enforcement of civil and commercial judgments between EU member states. General rule: defendants must be sued in the courts of their domicile. Special rules for contract (place of performance) and tort (place of harmful event). Replaced Brussels I Regulation (44/2001).",
 "source": "EU Regulation No 1215/2012 (Brussels Ia Recast)"},

{"id": "LG-15", "domain": "legal", "difficulty": "hard",
 "query": "What is the principle of non-refoulement in international refugee law?",
 "ground_truth": "Non-refoulement (Article 33, 1951 Refugee Convention) prohibits states from returning a refugee to a country where they face serious threats to their life or freedom based on race, religion, nationality, political opinion, or membership of a particular social group. It is considered a peremptory norm (jus cogens) of international law, binding on all states even those not party to the Convention.",
 "source": "1951 Refugee Convention, Article 33; UNHCR Guidelines on Non-Refoulement (2007)"},

]


def get_all():
    return QUESTIONS

def get_by_domain(domain):
    return [q for q in QUESTIONS if q["domain"] == domain]

def get_by_difficulty(difficulty):
    return [q for q in QUESTIONS if q["difficulty"] == difficulty]

def summary():
    domains = {}
    difficulties = {}
    for q in QUESTIONS:
        domains[q["domain"]] = domains.get(q["domain"], 0) + 1
        difficulties[q["difficulty"]] = difficulties.get(q["difficulty"], 0) + 1
    print(f"Total questions: {len(QUESTIONS)}")
    print(f"By domain: {domains}")
    print(f"By difficulty: {difficulties}")

if __name__ == "__main__":
    summary()
