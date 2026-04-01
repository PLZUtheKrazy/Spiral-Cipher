# Spiral-Cipher
소수를 이용한 카이사르 암호 변형으로, 글자가 위치한 자리에 따라 키가 달라집니다. / It's a variation of Caesar Cipher using primes; the key varies by where the character locates.

# 원리 / How it works

카이사르 암호에서 시작해, 자리마다 다른 해독 key를 주는 나선 암호를 발전시킨 버전입니다. / It's an advanced version of Caesar Cipher by giving decoding key based on location.
이번에는 소수를 이용해 key 값을 결정하여 더 예측하기 어렵고 강력한 암호를 만들었습니다. / This time, I used primes to decide keys to make a more complex,~~HARDER, BETTER, FASTER, ~~ STRONGER cipher.


# 특징 / Features

- **위치 의존적 암호**: 첫 번째 글자는 1번째 소수(2), 두 번째는 2번째 소수(3), 세 번째는 5, 네 번째는 7… 순으로 이동/*Location dependent shift**: It goes in order of 1st place, 1st decimal (2), 2nd place, 2nd  decimal (3), 3rd 5 and 4th 7…
- **알파벳 주기 처리**: shift 값이 26을 넘으면 `% 26`으로 나머지를 구해 A~Z (또는 a~z) 범위 안에서 안전하게 처리/**Alphabet periodic processing**: Get the remainder as '%26' when the shift value exceeds 26 and safely process it within the A-Z (or a-z) range
- 대소문자 모두 지원 / Support both case characters
- 공백, 숫자, 특수문자, 한글 등은 그대로 유지 (암호화되지 않음) / Keep spaces, numbers, special characters, Korean characters, etc. intact (not encrypted)
- 암호화와 복호화가 완벽하게 대칭 (원문 100% 복원) / Fully reversible encryption and decryption (100% original)

# 여담 / Trivia
- 이걸 만든 저는 16살로, 흔히 말하는 '급식이'입니다. / I'm 16 years old, so I'm still teenager making this.
- 영감은 수학잡지에서 얻었습니다. / I got inspired reading math magazines.
