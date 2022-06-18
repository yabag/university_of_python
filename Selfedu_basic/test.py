m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

a, b, c = map(int, input().split())

note1 = '#' + m[a - 1] if m[a - 1] == 'до' or m[a - 1] == 'фа' else m[a - 1]
note2 = '#' + m[b - 1] if m[b - 1] == 'до' or m[b - 1] == 'фа' else m[b - 1]
note3 = '#' + m[c - 1] if m[c - 1] == 'до' or m[c - 1] == 'фа' else m[c - 1]

print(note1, note2, note3)
