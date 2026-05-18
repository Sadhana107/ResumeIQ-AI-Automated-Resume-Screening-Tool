import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.text_extraction import (
    extract_pdf_text,
    extract_docx_text
)

from src.preprocess import clean_text


# =====================================================
# LOAD JOB DESCRIPTION
# =====================================================

with open(

    "data/job_description.txt",

    "r",

    encoding="utf-8"

) as f:

    job_description = f.read()

job_description = clean_text(job_description)


# =====================================================
# PROCESS RESUMES
# =====================================================

resume_folder = "resumes"

results = []

# CHECK FOLDER EXISTS

if not os.path.exists(resume_folder):

    print("\nERROR: resumes folder not found")

    exit()

resume_files = os.listdir(resume_folder)

# CHECK FILES EXIST

if len(resume_files) == 0:

    print("\nERROR: No resumes found inside resumes folder")

    exit()


for file in resume_files:

    file_path = os.path.join(
        resume_folder,
        file
    )

    text = ""

    try:

        # PDF
        if file.endswith(".pdf"):

            text = extract_pdf_text(file_path)

        # DOCX
        elif file.endswith(".docx"):

            text = extract_docx_text(file_path)

        else:
            continue

        # SKIP EMPTY TEXT
        if not text:

            continue

        cleaned_resume = clean_text(text)

        # =====================================================
        # TF-IDF
        # =====================================================

        documents = [

            job_description,

            cleaned_resume
        ]

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(

            vectors[0:1],

            vectors[1:2]

        )[0][0]

        score = round(
            similarity * 100,
            2
        )

        status = "Shortlisted"

        if score < 40:

            status = "Rejected"

        results.append({

            "Resume": file,

            "Score": score,

            "Status": status
        })

    except Exception as e:

        print(f"\nError processing {file}: {e}")


# =====================================================
# CHECK RESULTS
# =====================================================

if len(results) == 0:

    print("\nERROR: No valid resumes processed")

    exit()


# =====================================================
# CREATE DATAFRAME
# =====================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(

    by="Score",

    ascending=False
)

print("\nSCREENING RESULTS:\n")

print(results_df)


# =====================================================
# SAVE OUTPUT
# =====================================================

os.makedirs(
    "outputs",
    exist_ok=True
)

results_df.to_csv(

    "outputs/resume_screening_results.csv",

    index=False
)

print("\nSCREENING COMPLETED SUCCESSFULLY")