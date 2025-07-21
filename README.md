# ☁️ Cloud Resume Challenge (AWS Edition)



This repository contains my implementation of the Cloud Resume Challenge, a comprehensive project that combines front-end, back-end, DevOps, and modern cloud practices to build and deploy a technical resume on AWS. The challenge showcases skills in cloud architecture, serverless computing, CI/CD pipelines, and web development.

![0651f854-e9d9-400c-96c9-c53c010dd543](https://github.com/user-attachments/assets/8024c879-e7ba-4870-9616-3e71d6f9d1e4)


🔗 [Live Site](https://www.hugoleonor.com)

---

## ✅ Challenge Completed: 16/16 Tasks

### 🔸 Frontend (Resume in HTML/CSS/JS)

- [x] **HTML**: Resume crafted directly in HTML for a clean, accessible structure.

- [x] **CSS**: Custom styling using pure CSS for a professional and responsive design.

- [x] **Static Website**: Hosted in an AWS S3 bucket with static website hosting enabled.

- [x] **HTTPS**: Secured with Amazon CloudFront for HTTPS delivery and caching.

- [x] **DNS**: Custom domain configured via AWS Route 53, pointing to CloudFront.

- [x] **JavaScript**: Visitor counter implemented using a `fetch` call to a backend API.

### 🔸 Backend (API + Database)

- [x] **Database**: Visitor count stored in Amazon DynamoDB (on-demand mode).

- [x] **API**: REST API built with AWS API Gateway for secure and scalable access.

- [x] **Python**: AWS Lambda function written in Python using `boto3` to interact with DynamoDB.

- [x] **Tests**: Automated unit tests implemented with `pytest` for reliable backend functionality.

### 🔸 DevOps / Infrastructure

- [x] **Infrastructure as Code**: AWS resources defined and deployed using AWS SAM (`template.yaml`).

- [x] **Source Control**: Code versioned in separate GitHub repositories for frontend and backend.

- [x] **CI/CD (Backend)**: GitHub Actions pipeline for automated testing and deployment of the backend.

- [x] **CI/CD (Frontend)**: GitHub Actions pipeline to sync frontend code to S3 and invalidate CloudFront cache.

- [x] **Blog Post**: Read about my learnings here

---

## 🧱 Architecture

<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/a29030b8-59c9-4dde-aff6-3a97be9d7054" />


- **S3**: Stores HTML, CSS, and JavaScript files for the static resume website.
- **CloudFront**: Distributes content globally with HTTPS and caching for performance.
- **API Gateway**: Provides a secure REST endpoint for the visitor counter.
- **AWS Lambda**: Serverless function to increment and retrieve the visitor count.
- **DynamoDB**: NoSQL database for persistent storage of the visitor counter.

---


### 📁 Project Structure

```
cloud-resume/
├── frontend/
│   └── index.html           # Portfolio main webpage
├── backend/
│   ├── lambda_function.py   # AWS Lambda function (visitor counter code)
│   ├── lambda_function.zip  # Zipped Lambda function code (required by AWS Lambda)
│   └── tests/
│       └── test_lambda.py   # Unit tests for the Lambda function
├── infra/               
│   ├── acm.tf               # SSL certificate (AWS Certificate Manager)
│   ├── cloudfront.tf        # CloudFront CDN configuration
│   ├── dynamodb.tf          # DynamoDB table configuration
│   ├── iam.tf               # IAM roles and permissions
│   ├── lambda.tf            # Lambda deployment setup
│   ├── outputs.tf           # Terraform output variables
│   ├── provider.tf          # AWS provider configuration
│   ├── route53.tf           # DNS setup
│   ├── s3.tf                # S3 bucket for static website hosting
│   └── variables.tf         # Reusable input variables
└── README.md               

```

### ⚙️ CI/CD Workflows

#### Backend (SAM + Python)

- **File**: `.github/workflows/deploy-backend.yml`
- Runs `pytest` for automated testing.
- Deploys backend resources using AWS SAM (`sam package` and `sam deploy`).

#### Frontend (S3 + CloudFront)

- **File**: `.github/workflows/deploy-frontend.yml`
- Syncs frontend code to the S3 bucket.
- Invalidates CloudFront cache for instant updates.

---

## 📚 Technologies Used

- **AWS S3**: Static website hosting for the resume.
- **AWS CloudFront**: Secure content delivery with HTTPS and caching.
- **AWS Route 53**: DNS management for custom domain.
- **AWS API Gateway**: REST API for visitor counter functionality.
- **AWS Lambda**: Serverless compute for backend logic.
- **AWS DynamoDB**: NoSQL database for storing visitor counts.
- **AWS SAM CLI**: Infrastructure as Code for automated resource deployment.
- **GitHub Actions**: CI/CD pipelines for frontend and backend.
- **Python + boto3**: Backend logic and AWS SDK for DynamoDB integration.
- **HTML, CSS, JavaScript**: Frontend for the resume website.
- **pytest**: Unit testing for backend reliability.

---

## Final thoughts

Participating in the **Cloud Resume Challenge** was an incredibly enriching experience. This project allowed me to **consolidate my AWS knowledge** and deepen my practical skills in areas such as **Infrastructure as Code**, **CI/CD**, **Serverless**, and **Web Development**.

Throughout the challenge, I faced obstacles like the **initial configuration of CloudFront with HTTPS** and managing resources using **AWS SAM** and **Terraform** together. However, these challenges turned into great learning opportunities — especially around **deployment automation** and building **robust pipelines** with **GitHub Actions**.

Beyond the technical aspect, this project also gave me a new perspective on **cloud development best practices** and the importance of having a **production-oriented mindset** — focusing on **security**, **scalability**, and **efficiency**.

I now feel much more confident working with **core AWS services** and designing and implementing **end-to-end cloud solutions**.

--- 

## 📜 License

MIT License © Hugo Leonor
