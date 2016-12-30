#RSSI Signal Improvement

Radio ranging using RSSI generally considers three models: 
- small scale (spatial and temporal) multipath fading,
- medium scale (spatial) shadowing model
- large scale (spatial) path loss (PL) model 

**![rssi_model.png](https://lh4.googleusercontent.com/1Zi3tO954zQ9XgQgTstx4kLGqBytEpBECsWWXrWjt59MzvVDaFfdHVtbkQkNYz_Jg4Yx9bgUX2ydtPfu9K6_jLSUmFn6XMAU0kanSPuOlrviqHQ2rl1ueV8As1NS-mmi9-9_I8PB)**

Among them, multipath fading effect is unwanted and can be mitigated by filters. Shadowing model explains the slow signal-
strength fluctuation versus distance. This effect is caused by multipath signal propagation encounters reflection(s) and
diffraction. This effect can be emulated by ray tracing method. The last model, path loss model is an empirical model which describes the attenuation of signal strength versus distance. Path loss model is the only model that contributes to RSSI radio ranging.
RSS signal improvement is mainly to filter noise and fast fading effect. This increases the stability of the RSSI signal. 

Let's study about multipath effect: 
In wireless telecommunication, multi-path is the propagation phenomena that results in radio signals
reaching the receiving antenna by two or more paths.

</br>
In a typical wireless communication environment, multiple propagation paths exist between transmitter
and receiver due to scattering by different objects. Thus, copies of the signal following different paths can
undergo different attenuation, distortions, delays and phase shifts. Constructive and destructive interference can
occur at the receiver. When destructive interference occurs, the signal power can be significantly diminished.
This phenomenon is called fading.

- **Frequency Selective fading**: The transmitted signal reaching the receiver through multiple propagation paths,
having a different relative delay and amplitude. This is called multipath propagation and causes different parts
of the transmitted signal spectrum to be attenuated differently, which is known as frequency-selective fading.

- **Frequency Non-Selective fading**: If all the frequency components of the signal would roughly undergo the
same degree of fading, the channel is then classified as frequency non-selective (also called flat fading).

- **Slow fading**:
Slow fading is a long-term fading effect changing the mean value of the received signal. Slow fading is
usually associated with moving away from the transmitter and experiencing the expected reduction in signal
strength. Slow fading can be caused by events such as shadowing, where a large obstruction such as a hill or
large building obscures the main signal path between the transmitter and the receiver.

- **Fast fading**:
Fast fading is the short term component associated with multipath propagation. It is influenced by the
speed of the mobile terminal and the transmission bandwidth of the signal. In a fast fading channel, the rate of
change of the channel is higher than the signal symbol period and hence the channel changes over one period

This section describe methods that can help reduce the problem of fading in wireless communication channels. 
They are:
- Diversity for fast and slow fading 
- Equalization for flat and frequency selection fading
- Rake receiver for multipath fading
- Channel Coding for deep fading.

For details on individual techniques [click here]("")

[Click here]("") for an article on removal of fast fading effect using artificial neural networks. 
