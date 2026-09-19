![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Seismic Moment Magnitude Calculator
 
*For seismologists and earthquake hazard analysts: enter fault rupture dimensions, average slip, and shear modulus to compute seismic moment and moment magnitude Mw.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Seismology
 
This Gradio app estimates earthquake moment magnitude from simple fault rupture parameters. The user provides four numeric inputs in a single-column layout: fault rupture length in kilometers, fault width in kilometers, average slip in meters, and crustal shear modulus in gigapascals. Length and width are converted to meters; the rupture area is calculated as A = length × width. The shear modulus is converted to pascals by multiplying the GPa value by 1×10^9. Seismic moment is then computed as M0 = shear_modulus × rupture_area × average_slip, giving M0 in newton-meters. The moment magnitude is calculated using the standard relation Mw = (2/3) × log10(M0) − 6.03, where M0 is in N·m. The app also converts M0 to dyne·cm for users working with cgs convention. The Gradio UI uses a gr.Blocks layout with four gr.Number inputs (with sensible defaults such as 50 km length, 20 km width, 1.5 m slip, and 30 GPa shear modulus), a Run Calculation button, and two gr.Textbox outputs. Output 1 displays seismic moment in both N·m and dyne·cm in scientific notation. Output 2 displays moment magnitude rounded to two decimal places. No AI/ML component is used; this is a deterministic physical calculation that avoids the saturation issues of older magnitude scales.
 
## Run it
 
```bash
docker build -t seismic-moment-magnitude-calculator .
docker run -p 7860:7860 seismic-moment-magnitude-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-19.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
