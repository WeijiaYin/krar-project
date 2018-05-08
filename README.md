# ADL3

## Example usage

```
cat > lib.adl3 <<EOF
initially alive && !loaded
Load causes loaded during 2
Load releases loaded during 1
Shoot causes !loaded && !alive during 1
impossible Shoot if !loaded
EOF

cat > scenario.adl3s <<EOF
OBS:
ACS:
Load 1 2
Shoot 3 1
EOF

$ adl3 -l lib.adl3 -s scenario.adl3s -q "necessary executable Load, Shoot in 2"
False
```