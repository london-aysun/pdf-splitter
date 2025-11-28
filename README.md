
# PDF Splitter

## Overview
This project provides a Python-based solution to split a bulk PDF containing multiple certificates into individual PDF files. It supports automation for certificate distribution but can be used for any pdf.
---

## Architecture Diagram
```mermaid
flowchart LR
    subgraph CLI
        A[Command-Line Interface]
    end

    subgraph Core
        B[PDF Splitter Application]
        C[Error Handling & Logging]
        D[PDF Processing Library (PyPDF2)]
    end

    subgraph Testing
        E[Unit Tests (pytest)]
    end

    subgraph Deployment
        F[Docker Container]
        G[CI/CD Pipeline (GitHub Actions)]
    end
 

Important: your imput file must be named input.pdf;  Curreny script handles PF only.

---

##  Features
- Splits any PDF into separate pages
- Handles errors gracefully
- Easy to use with virtual environments

---

## Installation
Clone the repository and set up your environment:

```bash
git clone https://github.com/<your-username>/pdf-splitter.git
cd pdf-splitter


To Activate Virtual Env:

python3 -m venv ven

source venv/bin/activate

To Deactivate Virtual Env:

deactivate

+

pip install -r requirements.txt


