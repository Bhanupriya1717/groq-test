# Security Considerations

This project uses the Groq API. Below are key security threats and mitigations.

## 1. API Key Exposure
**Threat:** API key leaked in code or GitHub  
**Mitigation:** Store in `.env` and add `.env` to `.gitignore`

## 2. Prompt Injection
**Threat:** Malicious user input manipulating AI output  
**Mitigation:** Validate and sanitize inputs

## 3. API Abuse / Rate Limits
**Threat:** Too many requests causing service issues  
**Mitigation:** Use retry limits and exponential backoff

## 4. Sensitive Data Leakage
**Threat:** Sending personal or confidential data  
**Mitigation:** Avoid sending sensitive information to API

## 5. Logging Sensitive Information
**Threat:** Logs exposing secrets or private data  
**Mitigation:** Log only errors, never API keys or full responses