from cirron import Tracer

with Tracer() as t:
    print(2+3)

print(t.trace)