import re

α = '(-?\d*)'
β = re.compile(f'p=<{α},{α},{α}>, v=<{α},{α},{α}>, a=<{α},{α},{α}>')
χ = [list(map(int, β.match(π).groups())) for π in open('20.txt')]
δ = lambda ω: sum(map(abs, ω))
ε = min(χ, key=lambda σ: (δ(σ[6:]), δ(σ[3:6]), δ(σ[:3])))
φ = χ.index(ε)

print(φ)
