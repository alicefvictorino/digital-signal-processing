filename = "Church_Schellingwoude.wav";
new_record = false; % set to false if you want to reuse a previously recorded voice sample

% y is a matrix containing audio data, and each column represents a channel
% Fs is the sample rate (frequência de amostragem) in Hz
[y, Fs] = audioread(filename);

% the input audio is stereo (2 channels), so we extract only the first
% channel as required for the project
impulse_response = y(:, 1);

if new_record
    recorder = audiorecorder(Fs, 16, 1);
    recordblocking(recorder, 7);
    y_recorded = getaudiodata(recorder);
    
    save('voice.mat', 'y_recorded', 'recorder'); 
else
    load('voice.mat');
    if exist('recorder', 'var')
       y_recorded = getaudiodata(recorder);
    end
end

y_conv = conv(impulse_response, y_recorded);
y_conv_normalized = y_conv/max(abs(y_conv));

audiowrite('results.wav', y_conv_normalized, Fs);
 
soundsc(y_conv_normalized, Fs);