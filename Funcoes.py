import control as ctrl
import numpy as np

def erro_estacionario(G0, H0, C0):
  return 1 / (1 + (G0*H0*C0))

def k_proporcional(G0, H0, erro):
  k_p = ((1 / erro) - 1) / (G0*H0)
  return k_p

def margens_de_estabilidade(ftma):
  gm, pm, _, wpc, wgc, _ = ctrl.stability_margins(ftma)
  
  MG = gm  # Margem de ganho
  MF = pm  # Margem de fase
  freq0db = wgc  # Frequência de cruzamento de ganho (0 dB)
  freq180 = wpc  # Frequência de cruzamento de fase (-180°)
  fase_freq0db = pm - 180  # Fase na frequência de 0 dB
  ganho_freq180 = -(20 * np.log10(gm))  # Ganho na frequência de -180°

  return MG, MF, freq0db, freq180, fase_freq0db, ganho_freq180