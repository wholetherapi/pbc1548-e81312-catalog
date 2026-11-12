// tide_table — shipped firmware
// Patchbay Collective, rev r3

#include <Arduino.h>
#include "calibration.h"

constexpr uint8_t kDriverA = 5;
constexpr uint8_t kDriverB = 6;
constexpr uint8_t kDamping = 9;
constexpr uint8_t kCvA = A0;
constexpr uint8_t kCvB = A1;

static float damping_target = 0.5f;
static float damping_smooth = 0.5f;

void setup() {
  pinMode(kDriverA, OUTPUT);
  pinMode(kDriverB, OUTPUT);
  pinMode(kDamping, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  const int cv_a = analogRead(kCvA);
  const int cv_b = analogRead(kCvB);

  // Excite both resonators with short, alternating pulses.  The pulse
  // spacing spreads the excitation energy across the six resonator modes.
  digitalWrite(kDriverA, HIGH);
  delayMicroseconds(70);
  digitalWrite(kDriverA, LOW);

  delayMicroseconds(120 + (cv_a >> 3));
  digitalWrite(kDriverB, HIGH);
  delayMicroseconds(70);
  digitalWrite(kDriverB, LOW);

  damping_target = static_cast<float>(cv_b) / 1023.0f;
  damping_smooth += (damping_target - damping_smooth) * 0.05f;
  analogWrite(kDamping, static_cast<uint8_t>(damping_smooth * 255.0f));

  delayMicroseconds(900);
}
