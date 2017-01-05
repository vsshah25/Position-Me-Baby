#DIVERSITY

Diversity is a method used to develop information from several signals transmitted
over independent fading paths. It exploits the random nature of radio propagation
by finding independent signal paths for communication. It is a very simple concept
where if one path undergoes a deep fade, another independent path may have a
strong signal. As there is more than one path to select from, both the instantaneous
and average SNRs at the receiver may be improved.Receivers in diversity technique are used in such a
way that the signal received by one is independent of the other
We take up the types one by one in the sequel. 

##Space Diversity 
A method of transmission or reception, or both, in which the effects of fading are
minimized by the simultaneous use of two or more physically separated antennas,
ideally separated by one half or more wavelengths. 
</br>
pace diversity reception methods can be classified into four categories:
###Selection Diversity:
The basic principle of this type of diversity is selecting the signal which has the maximum SNR value among all
the signals received from different branches at the receiving end.
’M’ demodulators are used to provide M diversity branches whose gains are
adjusted to provide the same average SNR for each branch. The receiver branches
having the highest instantaneous SNR is connected to the demodulator. It is not an
optimal diversity technique as it doesn’t use all the possible branches simultaneously.

###Feedback or Scanning Diversity:
Scanning all the signals in a fixed sequence until the one with SNR more than a
predetermined threshold is identified. Quite similar to Selection diversity. 

###Maximal Ratio Combining:
Signals from all of the m branches are weighted according to their individual
signal voltage to noise power ratios and then summed. Requires an individual receiver and
phasing circuit for each antenna element. Produces an output SNR equal to the
sum of all individual SNR. Advantage of producing an output with an acceptable
SNR even when none of the individual signals are themselves acceptable.

###Equal Gain Combining:
In some cases it is not convenient to provide for the variable weighting capability
required for true maximal ratio combining. In such cases, the branch weights are
all set unity, but the signals from each branch are co-phased to provide equal gain
combining diversity. It allows the receiver to exploit signals that are simultaneously
received on each branch.

##Polarization Diversity
Polarization Diversity relies on the decorrelation of the two receive ports to achieve
diversity gain. The two receiver ports must remain cross-polarized. Polarization
Diversity at a base station does not require antenna spacing. Polarization diversity
combines pairs of antennas with orthogonal polarizations. Reflected signals can undergo polarization
changes depending on the channel. Pairing two complementary polarizations, this
scheme can immunize a system from polarization mismatches that would otherwise
cause signal fade. Polarization diversity has prove valuable at radio and mobile communication 
base stations since it is less susceptible to the near random orientations
of transmitting antennas.

##Frequency Diversity
In Frequency Diversity, the same information signal is transmitted and received
simultaneously on two or more independent fading carrier frequencies. Rationale
behind this technique is that frequencies separated by more than the coherence
bandwidth of the channel will be uncorrelated and will thus not experience the same
fades.The probability of simultaneous fading will be the product of the individual
fading probabilities.
</br>
Main disadvantage is that it requires spare bandwidth also as many receivers as there are channels used
for the frequency diversity. 

##Time Diversity
In time diversity, the signal representing the same information are sent over the
same channel at different times. Time diversity repeatedly transmits information at
time spacings that exceeds the coherence time of the channel. Multiple repetition
of the signal will be received with independent fading conditions, thereby providing
for diversity. A modern implementation of time diversity involves the use of RAKE
receiver for spread spectrum CDMA, where the multipath channel provides redun-
dancy in the transmitted message. Disadvantage is that it requires spare bandwidth
also as many receivers as there are channels used for the frequency diversity.
</br>

Two important types of time diversity application is discussed below. 
###RAKE Receiver
n CDMA spread spectrum systems, CDMA spreading codes are designed to provide
very low correlation between successive chips, propagation delay spread in the radio
channel provides multiple version of the transmitted signal at the receiver. Delaying
multipath components by more than a chip duration, will appear like uncorrelated
noise at a CDMA receiver. CDMA receiver may combine the time delayed versions
of the original signal to improve the signal to noise ratio at the receiver.
</br>
RAKE receiver collect the time shifted versions of the original signal by providing a sep-
arate correlation receiver for M strongest multipath components. Outputs of each
correlator are weighted to provide a better estimate of the transmitted signal than
provided by a single component. Demodulation and bit decisions are based on the
weighted output of the correlators.

Schematic of a RAKE receiver is shown below : 

**![image](https://lh3.googleusercontent.com/Q98G6LYKqbLVS9_5j9_bSePIjpCoflJ7M1TnyyfJ6sOTuu4OqVnWG2Lyf7ODnilbK1L38BUrLmZh4sIIBX1-4FZT5-cl943DucvfZqEZsP8WYMBMUOxMoDP9q1WaPo-9tGj2Eyd_)**

