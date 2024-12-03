# Projeto Compensadores no Domínio da Frequência

Este repositório contém código em Python para o design de compensadores no domínio da frequência.

Os compensadores implementados incluem:
- proporcional (P),
- proporcional-integral (PI),
- proporcional-derivativo (PD),
- proporcional-integral-derivativo (PID),
- atraso de fase (LAG), e
- avanço de fase (LEAD).

Cada compensador é implementado com sua respectiva função de transferência $C(s)$ e pode ser utilizado para analisar e projetar sistemas de controle, atendendo a requisitos específicos.

## Compensadores e Suas Funções de Transferência

### 1. Proposcional (P)  

$$C(s) = k_p$$

### 2. Proporcional-Integral (PI)  
É um caso especial do Atraso de Fase: $\alpha \to \infty$

$$C(s) = \frac{k_ps + k_i}{s} = k_p\frac{s +\frac{k_i}{k_p}}{s}$$

### 3. Proporcional-Derivativo (PD)  
É um caso especial do Avanço de Fase: $\alpha \to 0$

$$C(s) = k_p + k_ds$$

### 4. Proporcional-Integral-Derivativo (PID)  

$$C(s) = k_p+\frac{k_i}{s}+k_ds = \frac{k_ps + k_i + k_d s^2}{s}$$

### 5. Atraso de fase (LAG)

$$C(s) = K \frac{1 + sT}{1 + s\alpha T}, \quad \alpha > 1$$

### 6. Avanço de fase (LEAD)

$$C(s) = K \frac{1 + sT}{1 + s\alpha T}, \quad 0 < \alpha < 1$$

---

## Installation  
Clone este repositório utilizando:
```bash
git clone https://github.com/bianca-carvalho/ControlSystems.git
