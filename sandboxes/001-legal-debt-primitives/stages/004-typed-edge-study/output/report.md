# Legal Debt Probe Report

Sections found: 60
References found: 197
Findings found: 48

## Findings

### DanglingReference (high)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:68`
- Message: Section 1120 references missing Section 9999.
- Evidence: Historical checklists still cite Section 9999 and must be retired.

### DanglingReference (high)

- Source: `ky_auto_policy_notice_statute_synthetic.md:43`
- Message: Section 304.20.340 references missing Section 304.20.999.
- Evidence: Legacy retention maps still cite Section 304.20.999 and should be corrected.

### DanglingReference (high)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:69`
- Message: Section 304.39.087 references missing Section 304.39.888.
- Evidence: Legacy batch files that still refer to Section 304.39.888 shall be treated as stale until a reviewer confirms a current source.

### DanglingReference (high)

- Source: `ky_product_compliance_matrix_synthetic.md:25`
- Message: Section 2040 references missing Section 2055.
- Evidence: An archived control worksheet still references Section 2055.

### DanglingReference (high)

- Source: `ky_proof_of_insurance_regulation_synthetic.md:38`
- Message: Section 806.39.070.7 references missing Section 806.39.070.9.
- Evidence: The obsolete exception code table references Section 806.39.070.9.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:18`
- Message: Section 1020 and Section 1040 reference each other.
- Evidence: If rejection of tort limitation is alleged, the claim shall move to Section 1040. / If the rejection form is missing, the file shall return to Section 1020.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:23`
- Message: Section 1030 and Section 806.39.070.7 reference each other.
- Evidence: If electronic reporting is unavailable, Section 806.39.070.7 controls the exception path. / If the electronic reporting feed fails, the insurer shall preserve records under Section 1500 and notify the proof-card owner under Section 1030.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:43`
- Message: Section 1070 and Section 1120 reference each other.
- Evidence: The analyst may consult NAIC guidance before closing the escalation, but the source must be recorded in Section 1120. / The evidence packet shall include source excerpts for Section 304.20.340, proof-card documents from Section 1030, and external authority notes from Section 1070.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:52`
- Message: Section 1090 and Section 304.20.040 reference each other.
- Evidence: Notice workflow ownership begins when Section 304.20.040, Section 304.20.050, or Section 304.20.320 applies. / Any automobile notice workflow shall coordinate with proof of insurance under Section 304.39.117 and the internal notice queue in Section 1090.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:53`
- Message: Section 1090 and Section 1110 reference each other.
- Evidence: Producer communications under Section 1110 must remain synchronized with this workflow. / If the producer sends corrected data, the notice workflow in Section 1090 shall be reopened.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:57`
- Message: Section 1100 and Section 304.20.320 reference each other.
- Evidence: The adverse action letter shall explain the specific reason required by Section 304.20.320 and the review process in Section 304.20.330. / The adverse action letter template in Section 1100 implements this requirement.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:58`
- Message: Section 1100 and Section 304.20.360 reference each other.
- Evidence: Privacy content shall be checked against Section 304.20.360 and the evidence packet in Section 1120. / The notice owner shall document the effective version of any FCRA model notice relied upon in Section 1100.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:67`
- Message: Section 1120 and Section 304.20.340 reference each other.
- Evidence: The evidence packet shall include source excerpts for Section 304.20.340, proof-card documents from Section 1030, and external authority notes from Section 1070. / The insurer shall retain the adverse action evidence packet described in Section 1120 and the compliance archive described in Section 1500.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:72`
- Message: Section 1200 and Section 304.39.120 reference each other.
- Evidence: Applicant disclosure intake shall store the no-fault rejection election described in Section 304.39.120 and route missing election evidence to Section 1040. / The intake workflow in Section 1200 is responsible for storing the applicant's proof of election.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:77`
- Message: Section 1300 and Section 806.39.070.5 reference each other.
- Evidence: Digital proof exceptions arise when Section 806.39.070.5 cannot be satisfied by ordinary electronic card presentation. / If the insured relies on a digital card, the exception process in Section 1300 shall be followed.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:78`
- Message: Section 1300 and Section 1400 reference each other.
- Evidence: The exception owner shall consult Section 1400 before closing the request. / Printed proof fallback applies when the digital proof exception process in Section 1300 fails.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:87`
- Message: Section 1500 and Section 304.39.200 reference each other.
- Evidence: Records retention shall preserve basic reparation support under Section 304.39.200, adverse notice records under Section 304.20.340, electronic reporting exceptions under Section 806.39.070.7, and supervisory decisions under Section 1600. / Records supporting basic reparation benefits shall include proof-card evidence from Section 806.39.070.3, electronic reporting evidence from Section 806.39.070.4, and review packets from Section 1500.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:87`
- Message: Section 1500 and Section 304.20.340 reference each other.
- Evidence: Records retention shall preserve basic reparation support under Section 304.39.200, adverse notice records under Section 304.20.340, electronic reporting exceptions under Section 806.39.070.7, and supervisory decisions under Section 1600. / The insurer shall retain the adverse action evidence packet described in Section 1120 and the compliance archive described in Section 1500.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:87`
- Message: Section 1500 and Section 806.39.070.7 reference each other.
- Evidence: Records retention shall preserve basic reparation support under Section 304.39.200, adverse notice records under Section 304.20.340, electronic reporting exceptions under Section 806.39.070.7, and supervisory decisions under Section 1600. / If the electronic reporting feed fails, the insurer shall preserve records under Section 1500 and notify the proof-card owner under Section 1030.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:87`
- Message: Section 1500 and Section 1600 reference each other.
- Evidence: Records retention shall preserve basic reparation support under Section 304.39.200, adverse notice records under Section 304.20.340, electronic reporting exceptions under Section 806.39.070.7, and supervisory decisions under Section 1600. / Supervisory review shall assess whether errors in Section 1050, Section 1090, Section 1100, or Section 1500 are isolated.

### CircularReference (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:92`
- Message: Section 1600 and Section 1700 reference each other.
- Evidence: Systemic issues shall be escalated to Section 1700. / The audit may reopen Section 1600 if the trend suggests a control failure.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:7`
- Message: Section 304.20.020 and Section 304.39.110 reference each other.
- Evidence: Uninsured motorist coverage shall be coordinated with required minimum tort liability insurance under Section 304.39.110 and included coverages under Section 304.39.100. / Uninsured motorist coverage coordination shall follow Section 304.20.020.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:7`
- Message: Section 304.20.020 and Section 304.39.100 reference each other.
- Evidence: Uninsured motorist coverage shall be coordinated with required minimum tort liability insurance under Section 304.39.110 and included coverages under Section 304.39.100. / Included coverages shall support the right to basic reparation benefits in Section 304.39.030, the payment obligation in Section 304.39.040, and uninsured vehicle coordination in Section 304.20.020.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:8`
- Message: Section 304.20.020 and Section 304.39.070 reference each other.
- Evidence: If a claimant is a secured person, the analyst shall also review Section 304.39.070. / Recovery rights shall be coordinated with uninsured motorist coverage under Section 304.20.020.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:12`
- Message: Section 304.20.040 and Section 304.20.050 reference each other.
- Evidence: Cancellation, nonrenewal, and termination notices shall be evaluated under Section 304.20.050 and Section 304.20.060. / Nonpayment notices shall satisfy the cancellation rule in Section 304.20.040 and preserve the proof-card audit trail required by Section 304.39.117.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:12`
- Message: Section 304.20.040 and Section 304.20.060 reference each other.
- Evidence: Cancellation, nonrenewal, and termination notices shall be evaluated under Section 304.20.050 and Section 304.20.060. / Material misrepresentation review shall support cancellation under Section 304.20.040 and notice quality control under Section 304.20.050.

### CircularReference (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:32`
- Message: Section 304.20.320 and Section 304.20.330 reference each other.
- Evidence: A declination shall include a specific reason and shall be reviewable under Section 304.20.330. / Review of adverse underwriting action shall reference the original reason required by Section 304.20.320 and the records retained under Section 304.20.340.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:25`
- Message: Section 304.39.030 and Section 304.39.060 reference each other.
- Evidence: Tort limitation review shall also consider Section 304.39.060 before a bodily injury claim is routed to litigation. / The no-fault rejection workflow affects basic reparation benefits under Section 304.39.030 and applicant disclosures under Section 304.39.120.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:29`
- Message: Section 304.39.040 and Section 304.39.100 reference each other.
- Evidence: An obligor shall pay basic reparation benefits in accordance with included coverages described in Section 304.39.100. / Included coverages shall support the right to basic reparation benefits in Section 304.39.030, the payment obligation in Section 304.39.040, and uninsured vehicle coordination in Section 304.20.020.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:43`
- Message: Section 304.39.060 and Section 304.39.120 reference each other.
- Evidence: The no-fault rejection workflow affects basic reparation benefits under Section 304.39.030 and applicant disclosures under Section 304.39.120. / Applicant disclosures shall explain the election described in Section 304.39.060 and shall be retained under Section 304.39.200.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:58`
- Message: Section 304.39.083 and Section 806.39.070.6 reference each other.
- Evidence: Binder cancellation creates a reporting obligation under Section 304.39.085 and shall follow the Department reporting pathway in Section 806.39.070.6. / Cancellation reporting for binders shall implement Section 304.39.083 and shall update termination reporting under Section 304.39.085.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:64`
- Message: Section 304.39.085 and Section 806.39.070.4 reference each other.
- Evidence: Operational reporting shall follow Section 806.39.070.4 and Section 806.39.070.6. / Termination feeds shall be reconciled with Section 304.39.085 and exception handling in Section 806.39.070.7.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:64`
- Message: Section 304.39.085 and Section 806.39.070.6 reference each other.
- Evidence: Operational reporting shall follow Section 806.39.070.4 and Section 806.39.070.6. / Cancellation reporting for binders shall implement Section 304.39.083 and shall update termination reporting under Section 304.39.085.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:68`
- Message: Section 304.39.087 and Section 806.39.070.4 reference each other.
- Evidence: Vehicle identification number reporting shall support the verification requirements in Section 806.39.070.4. / Electronic coverage reporting shall use the policyholder and VIN data required by Section 304.39.087.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:88`
- Message: Section 304.39.117 and Section 806.39.070.2 reference each other.
- Evidence: Proof of insurance shall be provided in paper or electronic format and shall be administered under Section 806.39.070.2 and Section 806.39.070.3. / An insurer shall provide proof of insurance when a policy is issued, renewed, or amended to include a vehicle as required by Section 304.39.117.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:88`
- Message: Section 304.39.117 and Section 806.39.070.3 reference each other.
- Evidence: Proof of insurance shall be provided in paper or electronic format and shall be administered under Section 806.39.070.2 and Section 806.39.070.3. / Card content shall support presentation to a county clerk or peace officer under Section 806.39.070.5 and the proof obligation in Section 304.39.117.

### CircularReference (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:89`
- Message: Section 304.39.117 and Section 806.39.070.5 reference each other.
- Evidence: The card must be available to support county clerk and peace officer review described in Section 806.39.070.5. / Presentation rules shall support proof of insurance under Section 304.39.117 and printed card content under Section 806.39.070.3.

### CircularReference (medium)

- Source: `ky_proof_of_insurance_regulation_synthetic.md:13`
- Message: Section 806.39.070.2 and Section 806.39.070.8 reference each other.
- Evidence: Printed proof shall follow Section 806.39.070.3, and electronic proof shall follow Section 806.39.070.8. / The forms library shall maintain printed card templates under Section 806.39.070.3 and electronic card templates under Section 806.39.070.2.

### CircularReference (medium)

- Source: `ky_proof_of_insurance_regulation_synthetic.md:18`
- Message: Section 806.39.070.3 and Section 806.39.070.5 reference each other.
- Evidence: Card content shall support presentation to a county clerk or peace officer under Section 806.39.070.5 and the proof obligation in Section 304.39.117. / Presentation rules shall support proof of insurance under Section 304.39.117 and printed card content under Section 806.39.070.3.

### OrphanDefinition (low)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:17`
- Message: Defined term "No-fault rejection form" appears to be unused outside its definition.
- Evidence: - "No-fault rejection form" means a form used for an election described in Section 304.39.060.

### OrphanDefinition (low)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:18`
- Message: Defined term "Assigned risk policy" appears to be unused outside its definition.
- Evidence: - "Assigned risk policy" means coverage placed through a residual market mechanism.

### OrphanDefinition (low)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:20`
- Message: Defined term "Courier endorsement" appears to be unused outside its definition.
- Evidence: - "Courier endorsement" means an endorsement used only for retired courier programs.

### UnversionedExternalAuthority (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:43`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: The analyst may consult NAIC guidance before closing the escalation, but the source must be recorded in Section 1120.

### UnversionedExternalAuthority (medium)

- Source: `commonwealth_auto_claims_playbook_synthetic.md:48`
- Message: ISO is referenced without an obvious version, date, or effective source anchor.
- Evidence: The forms analyst shall review ISO circulars and carrier templates before approving the release.

### UnversionedExternalAuthority (medium)

- Source: `ky_auto_policy_notice_statute_synthetic.md:52`
- Message: FCRA is referenced without an obvious version, date, or effective source anchor.
- Evidence: Privacy and adverse action notices may require FCRA coordination when underwriting information is used.

### UnversionedExternalAuthority (medium)

- Source: `ky_motor_vehicle_insurance_code_synthetic.md:84`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: The liability review may use NAIC model bulletins if the bulletin year is recorded in the claim note.

### UnversionedExternalAuthority (medium)

- Source: `ky_product_compliance_matrix_synthetic.md:12`
- Message: NAIC is referenced without an obvious version, date, or effective source anchor.
- Evidence: The screen shall also record any NAIC reference by bulletin year.

### UnversionedExternalAuthority (medium)

- Source: `ky_proof_of_insurance_regulation_synthetic.md:44`
- Message: ISO is referenced without an obvious version, date, or effective source anchor.
- Evidence: The library shall not rely on ISO circulars without a versioned source note.

## Section Graph Edges

- Section 1000 -> Section 304.39.010 (`commonwealth_auto_claims_playbook_synthetic.md:8`)
- Section 1000 -> Section 304.39.080 (`commonwealth_auto_claims_playbook_synthetic.md:8`)
- Section 1000 -> Section 304.39.117 (`commonwealth_auto_claims_playbook_synthetic.md:8`)
- Section 1000 -> Section 304.20.040 (`commonwealth_auto_claims_playbook_synthetic.md:8`)
- Section 1000 -> Section 806.39.070.2 (`commonwealth_auto_claims_playbook_synthetic.md:8`)
- Section 1010 -> Section 304.39.030 (`commonwealth_auto_claims_playbook_synthetic.md:13`)
- Section 1010 -> Section 304.20.020 (`commonwealth_auto_claims_playbook_synthetic.md:13`)
- Section 1010 -> Section 304.20.040 (`commonwealth_auto_claims_playbook_synthetic.md:13`)
- Section 1010 -> Section 1020 (`commonwealth_auto_claims_playbook_synthetic.md:13`)
- Section 1010 -> Section 1030 (`commonwealth_auto_claims_playbook_synthetic.md:13`)
- Section 1020 -> Section 304.39.030 (`commonwealth_auto_claims_playbook_synthetic.md:17`)
- Section 1020 -> Section 304.39.040 (`commonwealth_auto_claims_playbook_synthetic.md:17`)
- Section 1020 -> Section 304.39.050 (`commonwealth_auto_claims_playbook_synthetic.md:17`)
- Section 1020 -> Section 1040 (`commonwealth_auto_claims_playbook_synthetic.md:18`)
- Section 1030 -> Section 304.39.117 (`commonwealth_auto_claims_playbook_synthetic.md:22`)
- Section 1030 -> Section 806.39.070.2 (`commonwealth_auto_claims_playbook_synthetic.md:22`)
- Section 1030 -> Section 806.39.070.3 (`commonwealth_auto_claims_playbook_synthetic.md:22`)
- Section 1030 -> Section 806.39.070.4 (`commonwealth_auto_claims_playbook_synthetic.md:22`)
- Section 1030 -> Section 806.39.070.7 (`commonwealth_auto_claims_playbook_synthetic.md:23`)
- Section 1040 -> Section 304.39.060 (`commonwealth_auto_claims_playbook_synthetic.md:27`)
- Section 1040 -> Section 304.39.120 (`commonwealth_auto_claims_playbook_synthetic.md:27`)
- Section 1040 -> Section 1020 (`commonwealth_auto_claims_playbook_synthetic.md:28`)
- Section 1050 -> Section 304.20.040 (`commonwealth_auto_claims_playbook_synthetic.md:32`)
- Section 1050 -> Section 304.20.050 (`commonwealth_auto_claims_playbook_synthetic.md:32`)
- Section 1050 -> Section 304.20.060 (`commonwealth_auto_claims_playbook_synthetic.md:32`)
- Section 1050 -> Section 304.39.085 (`commonwealth_auto_claims_playbook_synthetic.md:32`)
- Section 1050 -> Section 1090 (`commonwealth_auto_claims_playbook_synthetic.md:33`)
- Section 1060 -> Section 304.39.110 (`commonwealth_auto_claims_playbook_synthetic.md:37`)
- Section 1060 -> Section 304.20.020 (`commonwealth_auto_claims_playbook_synthetic.md:37`)
- Section 1060 -> Section 1070 (`commonwealth_auto_claims_playbook_synthetic.md:38`)
- Section 1070 -> Section 304.20.020 (`commonwealth_auto_claims_playbook_synthetic.md:42`)
- Section 1070 -> Section 304.39.070 (`commonwealth_auto_claims_playbook_synthetic.md:42`)
- Section 1070 -> Section 304.39.110 (`commonwealth_auto_claims_playbook_synthetic.md:42`)
- Section 1070 -> Section 1120 (`commonwealth_auto_claims_playbook_synthetic.md:43`)
- Section 1080 -> Section 806.39.070.8 (`commonwealth_auto_claims_playbook_synthetic.md:47`)
- Section 1080 -> Section 1030 (`commonwealth_auto_claims_playbook_synthetic.md:47`)
- Section 1090 -> Section 304.20.040 (`commonwealth_auto_claims_playbook_synthetic.md:52`)
- Section 1090 -> Section 304.20.050 (`commonwealth_auto_claims_playbook_synthetic.md:52`)
- Section 1090 -> Section 304.20.320 (`commonwealth_auto_claims_playbook_synthetic.md:52`)
- Section 1090 -> Section 1110 (`commonwealth_auto_claims_playbook_synthetic.md:53`)
- Section 1100 -> Section 304.20.320 (`commonwealth_auto_claims_playbook_synthetic.md:57`)
- Section 1100 -> Section 304.20.330 (`commonwealth_auto_claims_playbook_synthetic.md:57`)
- Section 1100 -> Section 304.20.360 (`commonwealth_auto_claims_playbook_synthetic.md:58`)
- Section 1100 -> Section 1120 (`commonwealth_auto_claims_playbook_synthetic.md:58`)
- Section 1110 -> Section 806.39.070.3 (`commonwealth_auto_claims_playbook_synthetic.md:62`)
- Section 1110 -> Section 1090 (`commonwealth_auto_claims_playbook_synthetic.md:62`)
- Section 1110 -> Section 1090 (`commonwealth_auto_claims_playbook_synthetic.md:63`)
- Section 1120 -> Section 304.20.340 (`commonwealth_auto_claims_playbook_synthetic.md:67`)
- Section 1120 -> Section 1030 (`commonwealth_auto_claims_playbook_synthetic.md:67`)
- Section 1120 -> Section 1070 (`commonwealth_auto_claims_playbook_synthetic.md:67`)
- Section 1120 -> Section 9999 (`commonwealth_auto_claims_playbook_synthetic.md:68`)
- Section 1200 -> Section 304.39.120 (`commonwealth_auto_claims_playbook_synthetic.md:72`)
- Section 1200 -> Section 1040 (`commonwealth_auto_claims_playbook_synthetic.md:72`)
- Section 1200 -> Section 1030 (`commonwealth_auto_claims_playbook_synthetic.md:73`)
- Section 1300 -> Section 806.39.070.5 (`commonwealth_auto_claims_playbook_synthetic.md:77`)
- Section 1300 -> Section 1400 (`commonwealth_auto_claims_playbook_synthetic.md:78`)
- Section 1400 -> Section 1300 (`commonwealth_auto_claims_playbook_synthetic.md:82`)
- Section 1400 -> Section 1500 (`commonwealth_auto_claims_playbook_synthetic.md:83`)
- Section 1500 -> Section 304.39.200 (`commonwealth_auto_claims_playbook_synthetic.md:87`)
- Section 1500 -> Section 304.20.340 (`commonwealth_auto_claims_playbook_synthetic.md:87`)
- Section 1500 -> Section 806.39.070.7 (`commonwealth_auto_claims_playbook_synthetic.md:87`)
- Section 1500 -> Section 1600 (`commonwealth_auto_claims_playbook_synthetic.md:87`)
- Section 1600 -> Section 1050 (`commonwealth_auto_claims_playbook_synthetic.md:91`)
- Section 1600 -> Section 1090 (`commonwealth_auto_claims_playbook_synthetic.md:91`)
- Section 1600 -> Section 1100 (`commonwealth_auto_claims_playbook_synthetic.md:91`)
- Section 1600 -> Section 1500 (`commonwealth_auto_claims_playbook_synthetic.md:91`)
- Section 1600 -> Section 1700 (`commonwealth_auto_claims_playbook_synthetic.md:92`)
- Section 1700 -> Section 1600 (`commonwealth_auto_claims_playbook_synthetic.md:96`)
- Section 1700 -> Section 1600 (`commonwealth_auto_claims_playbook_synthetic.md:97`)
- Section 304.20.020 -> Section 304.39.110 (`ky_auto_policy_notice_statute_synthetic.md:7`)
- Section 304.20.020 -> Section 304.39.100 (`ky_auto_policy_notice_statute_synthetic.md:7`)
- Section 304.20.020 -> Section 304.39.070 (`ky_auto_policy_notice_statute_synthetic.md:8`)
- Section 304.20.040 -> Section 304.20.050 (`ky_auto_policy_notice_statute_synthetic.md:12`)
- Section 304.20.040 -> Section 304.20.060 (`ky_auto_policy_notice_statute_synthetic.md:12`)
- Section 304.20.040 -> Section 304.39.117 (`ky_auto_policy_notice_statute_synthetic.md:13`)
- Section 304.20.040 -> Section 1090 (`ky_auto_policy_notice_statute_synthetic.md:13`)
- Section 304.20.050 -> Section 304.20.040 (`ky_auto_policy_notice_statute_synthetic.md:17`)
- Section 304.20.050 -> Section 304.39.117 (`ky_auto_policy_notice_statute_synthetic.md:17`)
- Section 304.20.050 -> Section 304.39.083 (`ky_auto_policy_notice_statute_synthetic.md:18`)
- Section 304.20.060 -> Section 304.20.040 (`ky_auto_policy_notice_statute_synthetic.md:22`)
- Section 304.20.060 -> Section 304.20.050 (`ky_auto_policy_notice_statute_synthetic.md:22`)
- Section 304.20.060 -> Section 304.20.340 (`ky_auto_policy_notice_statute_synthetic.md:23`)
- Section 304.20.300 -> Section 304.20.320 (`ky_auto_policy_notice_statute_synthetic.md:27`)
- Section 304.20.300 -> Section 304.20.330 (`ky_auto_policy_notice_statute_synthetic.md:27`)
- Section 304.20.300 -> Section 304.20.340 (`ky_auto_policy_notice_statute_synthetic.md:27`)
- Section 304.20.300 -> Section 304.20.350 (`ky_auto_policy_notice_statute_synthetic.md:27`)
- Section 304.20.300 -> Section 304.20.040 (`ky_auto_policy_notice_statute_synthetic.md:28`)
- Section 304.20.320 -> Section 304.20.330 (`ky_auto_policy_notice_statute_synthetic.md:32`)
- Section 304.20.320 -> Section 1100 (`ky_auto_policy_notice_statute_synthetic.md:33`)
- Section 304.20.330 -> Section 304.20.320 (`ky_auto_policy_notice_statute_synthetic.md:37`)
- Section 304.20.330 -> Section 304.20.340 (`ky_auto_policy_notice_statute_synthetic.md:37`)
- Section 304.20.330 -> Section 304.20.350 (`ky_auto_policy_notice_statute_synthetic.md:38`)
- Section 304.20.340 -> Section 1120 (`ky_auto_policy_notice_statute_synthetic.md:42`)
- Section 304.20.340 -> Section 1500 (`ky_auto_policy_notice_statute_synthetic.md:42`)
- Section 304.20.340 -> Section 304.20.999 (`ky_auto_policy_notice_statute_synthetic.md:43`)
- Section 304.20.350 -> Section 304.20.320 (`ky_auto_policy_notice_statute_synthetic.md:47`)
- Section 304.20.350 -> Section 304.20.340 (`ky_auto_policy_notice_statute_synthetic.md:47`)
- Section 304.20.350 -> Section 1600 (`ky_auto_policy_notice_statute_synthetic.md:48`)
- Section 304.20.360 -> Section 1100 (`ky_auto_policy_notice_statute_synthetic.md:53`)
- Section 304.39.010 -> Section 304.39.020 (`ky_motor_vehicle_insurance_code_synthetic.md:8`)
- Section 304.39.010 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:8`)
- Section 304.39.010 -> Section 304.39.100 (`ky_motor_vehicle_insurance_code_synthetic.md:8`)
- Section 304.39.010 -> Section 304.39.110 (`ky_motor_vehicle_insurance_code_synthetic.md:8`)
- Section 304.39.020 -> Section 304.39.070 (`ky_motor_vehicle_insurance_code_synthetic.md:14`)
- Section 304.39.020 -> Section 304.39.030 (`ky_motor_vehicle_insurance_code_synthetic.md:15`)
- Section 304.39.020 -> Section 304.39.040 (`ky_motor_vehicle_insurance_code_synthetic.md:15`)
- Section 304.39.020 -> Section 304.39.117 (`ky_motor_vehicle_insurance_code_synthetic.md:16`)
- Section 304.39.020 -> Section 806.39.070.2 (`ky_motor_vehicle_insurance_code_synthetic.md:16`)
- Section 304.39.020 -> Section 304.39.060 (`ky_motor_vehicle_insurance_code_synthetic.md:17`)
- Section 304.39.020 -> Section 304.39.085 (`ky_motor_vehicle_insurance_code_synthetic.md:19`)
- Section 304.39.030 -> Section 304.39.040 (`ky_motor_vehicle_insurance_code_synthetic.md:24`)
- Section 304.39.030 -> Section 304.39.050 (`ky_motor_vehicle_insurance_code_synthetic.md:24`)
- Section 304.39.030 -> Section 304.39.060 (`ky_motor_vehicle_insurance_code_synthetic.md:25`)
- Section 304.39.040 -> Section 304.39.100 (`ky_motor_vehicle_insurance_code_synthetic.md:29`)
- Section 304.39.040 -> Section 304.39.110 (`ky_motor_vehicle_insurance_code_synthetic.md:30`)
- Section 304.39.040 -> Section 304.39.200 (`ky_motor_vehicle_insurance_code_synthetic.md:30`)
- Section 304.39.045 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:34`)
- Section 304.39.045 -> Section 304.39.110 (`ky_motor_vehicle_insurance_code_synthetic.md:34`)
- Section 304.39.045 -> Section 806.39.070.5 (`ky_motor_vehicle_insurance_code_synthetic.md:34`)
- Section 304.39.050 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:38`)
- Section 304.39.050 -> Section 304.39.090 (`ky_motor_vehicle_insurance_code_synthetic.md:38`)
- Section 304.39.050 -> Section 304.39.085 (`ky_motor_vehicle_insurance_code_synthetic.md:39`)
- Section 304.39.060 -> Section 304.39.030 (`ky_motor_vehicle_insurance_code_synthetic.md:43`)
- Section 304.39.060 -> Section 304.39.120 (`ky_motor_vehicle_insurance_code_synthetic.md:43`)
- Section 304.39.060 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:44`)
- Section 304.39.070 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:48`)
- Section 304.39.070 -> Section 304.39.090 (`ky_motor_vehicle_insurance_code_synthetic.md:48`)
- Section 304.39.070 -> Section 304.20.020 (`ky_motor_vehicle_insurance_code_synthetic.md:49`)
- Section 304.39.080 -> Section 304.39.090 (`ky_motor_vehicle_insurance_code_synthetic.md:53`)
- Section 304.39.080 -> Section 304.39.100 (`ky_motor_vehicle_insurance_code_synthetic.md:53`)
- Section 304.39.080 -> Section 304.39.117 (`ky_motor_vehicle_insurance_code_synthetic.md:53`)
- Section 304.39.080 -> Section 806.39.070.2 (`ky_motor_vehicle_insurance_code_synthetic.md:54`)
- Section 304.39.083 -> Section 304.39.085 (`ky_motor_vehicle_insurance_code_synthetic.md:58`)
- Section 304.39.083 -> Section 806.39.070.6 (`ky_motor_vehicle_insurance_code_synthetic.md:58`)
- Section 304.39.083 -> Section 304.39.080 (`ky_motor_vehicle_insurance_code_synthetic.md:59`)
- Section 304.39.085 -> Section 304.39.087 (`ky_motor_vehicle_insurance_code_synthetic.md:63`)
- Section 304.39.085 -> Section 806.39.070.4 (`ky_motor_vehicle_insurance_code_synthetic.md:64`)
- Section 304.39.085 -> Section 806.39.070.6 (`ky_motor_vehicle_insurance_code_synthetic.md:64`)
- Section 304.39.087 -> Section 806.39.070.4 (`ky_motor_vehicle_insurance_code_synthetic.md:68`)
- Section 304.39.087 -> Section 304.39.888 (`ky_motor_vehicle_insurance_code_synthetic.md:69`)
- Section 304.39.090 -> Section 304.39.100 (`ky_motor_vehicle_insurance_code_synthetic.md:73`)
- Section 304.39.090 -> Section 304.39.110 (`ky_motor_vehicle_insurance_code_synthetic.md:73`)
- Section 304.39.090 -> Section 304.39.117 (`ky_motor_vehicle_insurance_code_synthetic.md:74`)
- Section 304.39.100 -> Section 304.39.030 (`ky_motor_vehicle_insurance_code_synthetic.md:78`)
- Section 304.39.100 -> Section 304.39.040 (`ky_motor_vehicle_insurance_code_synthetic.md:78`)
- Section 304.39.100 -> Section 304.20.020 (`ky_motor_vehicle_insurance_code_synthetic.md:78`)
- Section 304.39.110 -> Section 304.20.040 (`ky_motor_vehicle_insurance_code_synthetic.md:82`)
- Section 304.39.110 -> Section 304.20.020 (`ky_motor_vehicle_insurance_code_synthetic.md:83`)
- Section 304.39.117 -> Section 806.39.070.2 (`ky_motor_vehicle_insurance_code_synthetic.md:88`)
- Section 304.39.117 -> Section 806.39.070.3 (`ky_motor_vehicle_insurance_code_synthetic.md:88`)
- Section 304.39.117 -> Section 806.39.070.5 (`ky_motor_vehicle_insurance_code_synthetic.md:89`)
- Section 304.39.120 -> Section 304.39.060 (`ky_motor_vehicle_insurance_code_synthetic.md:93`)
- Section 304.39.120 -> Section 304.39.200 (`ky_motor_vehicle_insurance_code_synthetic.md:93`)
- Section 304.39.120 -> Section 1200 (`ky_motor_vehicle_insurance_code_synthetic.md:94`)
- Section 304.39.200 -> Section 806.39.070.3 (`ky_motor_vehicle_insurance_code_synthetic.md:98`)
- Section 304.39.200 -> Section 806.39.070.4 (`ky_motor_vehicle_insurance_code_synthetic.md:98`)
- Section 304.39.200 -> Section 1500 (`ky_motor_vehicle_insurance_code_synthetic.md:98`)
- Section 2000 -> Section 304.39.080 (`ky_product_compliance_matrix_synthetic.md:7`)
- Section 2000 -> Section 304.39.100 (`ky_product_compliance_matrix_synthetic.md:7`)
- Section 2000 -> Section 304.39.110 (`ky_product_compliance_matrix_synthetic.md:7`)
- Section 2000 -> Section 304.20.020 (`ky_product_compliance_matrix_synthetic.md:7`)
- Section 2000 -> Section 806.39.070.8 (`ky_product_compliance_matrix_synthetic.md:7`)
- Section 2010 -> Section 806.39.070.8 (`ky_product_compliance_matrix_synthetic.md:11`)
- Section 2010 -> Section 1100 (`ky_product_compliance_matrix_synthetic.md:11`)
- Section 2020 -> Section 806.39.070.3 (`ky_product_compliance_matrix_synthetic.md:16`)
- Section 2020 -> Section 806.39.070.8 (`ky_product_compliance_matrix_synthetic.md:16`)
- Section 2020 -> Section 1080 (`ky_product_compliance_matrix_synthetic.md:16`)
- Section 2030 -> Section 1030 (`ky_product_compliance_matrix_synthetic.md:20`)
- Section 2030 -> Section 1110 (`ky_product_compliance_matrix_synthetic.md:20`)
- Section 2030 -> Section 1400 (`ky_product_compliance_matrix_synthetic.md:20`)
- Section 2040 -> Section 2000 (`ky_product_compliance_matrix_synthetic.md:24`)
- Section 2040 -> Section 2010 (`ky_product_compliance_matrix_synthetic.md:24`)
- Section 2040 -> Section 2020 (`ky_product_compliance_matrix_synthetic.md:24`)
- Section 2040 -> Section 2030 (`ky_product_compliance_matrix_synthetic.md:24`)
- Section 2040 -> Section 1600 (`ky_product_compliance_matrix_synthetic.md:24`)
- Section 2040 -> Section 2055 (`ky_product_compliance_matrix_synthetic.md:25`)
- Section 806.39.070.1 -> Section 304.39.080 (`ky_proof_of_insurance_regulation_synthetic.md:7`)
- Section 806.39.070.1 -> Section 304.39.117 (`ky_proof_of_insurance_regulation_synthetic.md:8`)
- Section 806.39.070.2 -> Section 304.39.117 (`ky_proof_of_insurance_regulation_synthetic.md:12`)
- Section 806.39.070.2 -> Section 806.39.070.3 (`ky_proof_of_insurance_regulation_synthetic.md:13`)
- Section 806.39.070.2 -> Section 806.39.070.8 (`ky_proof_of_insurance_regulation_synthetic.md:13`)
- Section 806.39.070.3 -> Section 806.39.070.5 (`ky_proof_of_insurance_regulation_synthetic.md:18`)
- Section 806.39.070.3 -> Section 304.39.117 (`ky_proof_of_insurance_regulation_synthetic.md:18`)
- Section 806.39.070.4 -> Section 304.39.087 (`ky_proof_of_insurance_regulation_synthetic.md:22`)
- Section 806.39.070.4 -> Section 304.39.085 (`ky_proof_of_insurance_regulation_synthetic.md:23`)
- Section 806.39.070.4 -> Section 806.39.070.7 (`ky_proof_of_insurance_regulation_synthetic.md:23`)
- Section 806.39.070.5 -> Section 304.39.117 (`ky_proof_of_insurance_regulation_synthetic.md:27`)
- Section 806.39.070.5 -> Section 806.39.070.3 (`ky_proof_of_insurance_regulation_synthetic.md:27`)
- Section 806.39.070.5 -> Section 1300 (`ky_proof_of_insurance_regulation_synthetic.md:28`)
- Section 806.39.070.6 -> Section 304.39.083 (`ky_proof_of_insurance_regulation_synthetic.md:32`)
- Section 806.39.070.6 -> Section 304.39.085 (`ky_proof_of_insurance_regulation_synthetic.md:32`)
- Section 806.39.070.6 -> Section 806.39.070.4 (`ky_proof_of_insurance_regulation_synthetic.md:33`)
- Section 806.39.070.7 -> Section 1500 (`ky_proof_of_insurance_regulation_synthetic.md:37`)
- Section 806.39.070.7 -> Section 1030 (`ky_proof_of_insurance_regulation_synthetic.md:37`)
- Section 806.39.070.7 -> Section 806.39.070.9 (`ky_proof_of_insurance_regulation_synthetic.md:38`)
- Section 806.39.070.8 -> Section 806.39.070.3 (`ky_proof_of_insurance_regulation_synthetic.md:42`)
- Section 806.39.070.8 -> Section 806.39.070.2 (`ky_proof_of_insurance_regulation_synthetic.md:42`)

## Matrix Outputs

Matrix direction: `A[i,j] = 1` means node `i` depends on node `j`.

- `section_index.csv`: matrix node index and labels
- `adjacency_matrix.csv`: direct dependency matrix `A`
- `two_hop_matrix.csv`: boolean matrix product `A^2`
- `transitive_closure.csv`: all reachable dependencies
- `dependency_roots.json`: terminal dependency roots and cycle nodes

## Dependency Roots

- `section:1000` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1010` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1020` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1030` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1040` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1050` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1060` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1070` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1080` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1090` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1100` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1110` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1120` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1200` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1300` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1400` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1500` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1600` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:1700` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.020` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.040` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.050` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.060` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.300` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.320` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.330` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.340` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.350` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.20.360` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.010` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.020` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.030` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.040` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.045` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.050` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.060` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.070` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.080` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.083` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.085` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.087` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.090` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.100` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.110` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.117` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.120` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:304.39.200` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:2000` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:2010` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:2020` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:2030` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:2040` -> `missing:2055`, `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.1` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.2` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.3` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.4` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.5` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.6` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.7` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`
- `section:806.39.070.8` -> `missing:304.20.999`, `missing:304.39.888`, `missing:806.39.070.9`, `missing:9999`

## Cycle Nodes

- `section:1020`
- `section:1030`
- `section:1040`
- `section:1050`
- `section:1070`
- `section:1090`
- `section:1100`
- `section:1110`
- `section:1120`
- `section:1200`
- `section:1300`
- `section:1400`
- `section:1500`
- `section:1600`
- `section:1700`
- `section:304.20.020`
- `section:304.20.040`
- `section:304.20.050`
- `section:304.20.060`
- `section:304.20.320`
- `section:304.20.330`
- `section:304.20.340`
- `section:304.20.350`
- `section:304.20.360`
- `section:304.39.030`
- `section:304.39.040`
- `section:304.39.050`
- `section:304.39.060`
- `section:304.39.070`
- `section:304.39.080`
- `section:304.39.083`
- `section:304.39.085`
- `section:304.39.087`
- `section:304.39.090`
- `section:304.39.100`
- `section:304.39.110`
- `section:304.39.117`
- `section:304.39.120`
- `section:304.39.200`
- `section:806.39.070.2`
- `section:806.39.070.3`
- `section:806.39.070.4`
- `section:806.39.070.5`
- `section:806.39.070.6`
- `section:806.39.070.7`
- `section:806.39.070.8`
