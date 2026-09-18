# Consistency items for the final pass

Collected from the revision agents. Each is a cross-section problem that no single agent owns.

1. The method-row denominator moved from 110 to 112 when `helix_2025` and `groot_n16_2025` were
   added during review. Sections 3 to 7 still say 110. Every denominator must be recomputed at the
   same commit and stated once, in section 1 or in the method appendix, then used consistently.
   The code-releasing denominator moved from 61 to 62 for the same reason.
2. `groot_n16_2025` carries an untriaged `paper_code_mismatch`, so the mismatch classification is
   incomplete by one row. Either classify it or exclude it and say so.
3. `paper/sections/09_conclusion.md` cites section 8.10, which no longer exists after section 8 was
   cut to six gaps.
4. The interpenetration thread changed meaning during revision. It is no longer that engines hide
   penetration, which is refuted by Isaac Gym's own released code, but that the tooling exists and
   nobody records the number. Sections 1, 5, 7, 8 and 9 must all state the new version.
5. The contradiction count moved from 37 to 16 to 10 across three corrections. Only 10 is current.
6. Section 6's bimanual denominator and section 8's must agree. Section 6 is authoritative.
7. Table 6's cells are truncated mid-word and a reviewer could not read them. Widen the cap or
   restructure the table.
8. Figure 6 draws six bars where section 7's text describes five.
9. Appendices B and C are promised by the outline and do not exist.
10. The survey's own statistics measure what the extraction captured. Every such number is a floor.
    The disclosure belongs in section 7, in the method appendix, and anywhere a coverage percentage
    appears.
