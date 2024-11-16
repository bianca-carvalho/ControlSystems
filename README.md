# Compensator Design via Root Locus Diagrams  

This repository contains Python code for designing compensators using root locus diagrams. The compensators implemented include proportional (P), proportional-integral (PI), proportional-derivative (PD), proportional-integral-derivative (PID), phase-lag, and phase-lead compensators.  

Each compensator is implemented with its respective transfer function \( C(s) \) and can be used to analyze and design control systems to meet specific performance requirements.  

---

## Compensators and Their Transfer Functions  

### 1. Proportional (P)  
Transfer function:  
\[
C(s) = K_p
\]  

### 2. Proportional-Integral (PI)  
Transfer function:  
\[
C(s) = K_p \left( 1 + \frac{1}{T_i s} \right) = K_p + \frac{K_p}{T_i s}
\]  

### 3. Proportional-Derivative (PD)  
Transfer function:  
\[
C(s) = K_p \left( 1 + T_d s \right) = K_p + K_p T_d s
\]  

### 4. Proportional-Integral-Derivative (PID)  
Transfer function:  
\[
C(s) = K_p \left( 1 + \frac{1}{T_i s} + T_d s \right) = K_p + \frac{K_p}{T_i s} + K_p T_d s
\]  

### 5. Phase-Lag Compensator  
Transfer function:  
\[
C(s) = K \frac{T s + 1}{\beta T s + 1}, \quad \beta > 1
\]  

### 6. Phase-Lead Compensator  
Transfer function:  
\[
C(s) = K \frac{\beta T s + 1}{T s + 1}, \quad \beta > 1
\]  

---

## Usage  
Each Python script is designed to work with root locus diagrams, enabling you to analyze the system and adjust the compensator parameters to achieve desired performance.  

---

## Installation  
Clone this repository using:  
```bash
git clone https://github.com/bianca-carvalho/ControlSystems.git
