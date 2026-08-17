Amazon Textract is a fully managed machine learning service that goes beyond simple Optical Character Recognition (OCR) to automatically extract text, handwriting, and _structured data_ from scanned documents like PDFs and images.

### AIP-C01 Blueprint Breakdown:

#### 1. Benefits (AIP-C01 Focus)

Textract provides significant advantages by automating manual data entry, processing documents at scale, and,critically, understanding the _context_ of data:

- **Fully Managed:** Pre-trained models require no machine learning experience, allowing any developer to integrate document analysis.

- **Structured Data Extraction:** Instead of returning a raw text dump, Textract can differentiate tables and form fields (key-value pairs), preserving the relationship of data.

- **Scale & Speed:** Textract is built to handle millions of pages quickly, replacing slow and error-prone manual processing.


#### 2. When to Use (AIP-C01 Exam Triggers)

If a scenario describes one of the following, Amazon Textract is the correct choice:

- **Processing Scanned Docs:** When you need to read unstructured data from non-text files like PDFs, TIFFs, or JPEGs (not standard text-based files).

- **Extracting Tables or Forms:** When you need specific data fields from a form or data structured in a table (e.g.,invoice line items or bank statement rows).

- **Handwritten Notes:** Textract can accurately extract handwriting from documents like prescriptions or field reports.

- **Identify Documents:** For specialized tasks like automatically detecting driver's licenses, passports, or invoices.
#### 3. Cost Structure (Pay-As-You-Go)

You are charged per page processed, with different costs based on which API features you use:

- **Detect Document Text API:** Lowest cost for simple raw text extraction.

- **Analyze Document API - Tables/Forms:** Separate, slightly higher costs for extracting tabular or form field data.

- _Note for AIP-C01:_ There are specialized APIs for Invoices/Receipts (Analyze Expense) and ID documents (Analyze ID) that also have distinct pricing.
#### 4. Key Use Cases

Textract is widely used for:

- **Automated Invoice Processing:** Extracting data like invoice numbers, dates, and amounts for accounts payable.

- **Claims Processing:** Digitizing and processing insurance claim forms.

- **Digital Medical Records:** Extracting patient data from intake forms and notes.


The blueprint infographic provides a complete visual map of these concepts, including a workflow summary of how the service functions and the core pillars upon which it is built.![[Amazon Textract.png]]