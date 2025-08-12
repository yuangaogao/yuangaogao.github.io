+++
title = "Research | Dr. Yuan Gao"
+++
# Recent Projects

### <div id="dislocations">1. Macroscopic Dynamics for Nonequilibrium Chemical Reactions </div>

Most biochemical reactions in living cells are an open system interacting with the environment through chemostats. At a mesoscopic scale, the molecular number of each species in those biochemical reactions can be modeled by the random time-changed Poisson processes.

To characterize the macroscopic behaviors in the large volume limit, the law of large numbers in path space determines a mean-field limit nonlinear ODE. At the same time, the WKB expansion yields a Hamilton-Jacobi equation and the corresponding Lagrangian gives the good rate function in the large deviation principle (LDP). The rigorous convergence of Varadhan's discrete nonlinear semigroup (recast as a monotone scheme) to the continuous Lax-Oleinik semigroup yields the large deviation principle for the chemical reaction process at any single time. Consequently, the macroscopic mean-field limit reaction rate equation is recovered. Moreover, the LDP for invariant measures can be used to construct the global energy landscape for non-equilibrium reactions. This enables the dissipative-conservative decomposition for the Hamilton dynamics of chemical reactions, which also facilitates the understanding of thermodynamics.

The LDP for the invariant measure also provides a selection principle that selects a unique weak KAM solution to the corresponding stationary HJE. The weak KAM solutions for stationary Hamilton-Jacobi equations (HJE) is a key tool to study the long time behaviors of dynamical systems, such as the Mather measures or invariant sets. However, there are in general an infinite number of weak KAM solutions. The selected weak KAM solution has a variational principle with globally determined boundary values at the Aubry set and the Peierls barriers computed from the least action cost in an infinite time horizon starting from points in the Aubry set.  

<table border="0" width="900px" style="margin-top:30px;margin-bottom:-30px;"/>
    <center>
        <img src="fischer-crebs.jpeg" style="width:800px;"/>
    </center>
    <center style="zoom:100%;">
        2-autocatalysis non-equilibrium chemical reaction
    </center>
</table>

<table border="0" width="900px" style="margin-top:0px;margin-bottom:10px;"/>
    <tr>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="Escher_p3_012_nWU.pdf" style="margin-right:10px; margin-left:0px; width:300px; height:380px;"/>
            </center>
            <center style="zoom:100%; margin-right:10px;">
                Borrow from M.C. Escher
            </center>           
        </td>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="p3_012_nWU.pdf" style="margin-right:10px; margin-left:0px; width:300px;"/>
            </center>
            <center style="zoom:100%; margin-left:0px;">
                Global energy landscape serves as a selected weak KAM solution
            </center>
        </td>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="Sketch-R-n.pdf" style="margin-right:10px; margin-left:10px; width:450px;"/>
            </center>
            <center style="zoom:100%; margin-right:10px;">
                Decomposition and thermodynamics for <br> non-equilibrium chemical reaction with non-equilibrium stationary state (NESS)
            </center>           
        </td>
    </tr>
</table>

**Related publications:**

1. Gao, Y., and J. -G. Liu. <a href="https://link.springer.com/article/10.1007/s10955-022-02985-5" target="_blank">Revisit of macroscopic dynamics for some non-equilibrium chemical reactions from a Hamiltonian viewpoint</a>. Journal of Statistical Physics. 189(22). (2022).  *Full text:* <a href=/GL2022-JSP.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao, Y., and J. -G. Liu. <a href="https://doi.org/10.4208/cicp.OA-2023-0021" target="_blank">Random walk approximation for irreversible drift-diffusion process on manifold: ergodicity, unconditional stability and convergence</a>. Communications in Computational Physics. 34(1): 132-172. (2023).  *Full text:* <a href=/Gao_Liu_CICP23.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Gao, Y. and J. -G. Liu. <a href="https://doi.org/10.1137/22M1505633" target="_blank">Large deviation principle and thermodynamic limit of chemical master equation via nonlinear semigroup</a>. Multiscale Modeling and Simulation. 21(4): 1534-1569. (2023).  *Full text:* <a href=/GL2023-MMS.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
4. Gao, Y., and Y. F. Zhou. <a href="https://doi.org/10.4208/cmaa.2023-0003" target="_blank">Hamilton Dynamics in Chemical Reactions: the Maupertuis Principle, Transition Paths and Energy Landscape</a>. Communications in Mathematical Analysis and Applications, 2(3): 245-288. (2023).  *Full text:* <a href=/GZ2023.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
5. Gao, Y., and J. -G. Liu. <a href="https://doi.org/10.1137/22M1519717" target="_blank">A selection principle for weak KAM solutions via Freidlin-Wentzell large deviation principle of invariant measures</a>. SIAM Journal on Mathematical Analysis, 55(6): 6457-6495. (2023). *Full text:* <a href=/GL2023-JMA.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

### <div id="dislocations">2. Optimal control and mean field game for chemical reactions and particle systems </div>

Optimal control for single particle and mean-field control for interacting particle system has broad applications across interdisciplinary fields such as biology, physics, materials science, data science, and social sciences. In these interactive dynamics, non-typical trajectories with large fluctuations occur with small probability but are fundamental events such as protein folding and species evolution/extinction. A fundamental question is to predict and control these non-typical behaviors in interactive dynamics on complex configuration spaces, such as transition paths between metastable states on chemical reaction networks.

We explore a stochastic optimal control formulation for transition path problems in an infinite time horizon, for both dynamics modeled by diffusion processes or Markov jump processes on Polish spaces. An unbounded terminal cost at a stopping time, along with a controlled transition rate, regulates the transitions between metastable states. The optimal control to proved to maintain the original bridges with the running cost suggested by the rate function in the large deviation principle. Girsanov transforms and Gamma-convergence techniques will be adapted to justify the singular optimal control. The optimally controlled process realizes the transition paths almost surely but without altering the bridges of the original process.

Mean field games and mean field control model the collective behaviors of interacting individual/particles, which can be regarded as the mean field limit of N-player games or N-particle system. The resulting optimal control problem is an optimization problem in a probability density space equipped with Wasserstein metrics. For a discrete configuration space, analogous Nash systems and master equations can be derived with variational principles. The associated continuity equation on a graph with a nonlinear activation function generalizes the usual discrete Wasserstein metrics. The variational principle can also be generalized to non-potential games given the information of Nash equilibriums. For a continuous configuration space, the homogenization of the Wasserstein distance and the Wasserstein gradient flow structure for the mean field limit PDE can be proved by evolutionary Gamma-convergence techniques and the variational principles. The exchange of mean field limit, the large time limit and the oscillation parameters in the homogenization limit is a challenging open question.

<table border="0" width="900px" style="margin-top:30px;margin-bottom:-30px;"/>
    <center>
        <img src="gradient.jpeg" style="width:800px;"/>
    </center>
    <center style="zoom:100%;">
        Optimal control formulation for rare events and transition paths between metastable sets
    </center>
</table>
<table border="0" width="900px" style="margin-top:30px;margin-bottom:-30px;"/>
    <center>
        <img src="10_KLD.jpeg" style="width:800px;"/>
    </center>
    <center style="zoom:100%;">
        Mean-field control for complex fluid with different loss
    </center>
</table>
<table border="0" width="900px" style="margin-top:30px;margin-bottom:-30px;"/>
    <center>
        <img src="herding_behavior.jpeg" style="width:800px;"/>
    </center>
    <center style="zoom:100%;">
        Collective behaviors for large number of particles
    </center>
</table>

**Related publications:**
1. Gao, Y., T. Li, X. Li, and J. -G. Liu. <a href="https://epubs.siam.org/doi/10.1137/21M1437883" target="_blank">Transition path theory for Langevin dynamics on manifold: optimal control and data-driven solver</a>. Multiscale Modeling and Simulation. 21(1): 1-33. (2023). *Full text:* <a href=/GLLL2023.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao, Y., W. Li, and J. -G. Liu. <a href="https://doi.org/10.3934/dcdsb.2023204" target="_blank">Master equations for finite state mean field games with nonlinear activations</a>. Discrete and Continuous Dynamical Systems Series B, 29(7): 2837-2879. (2024). *Full text:* <a href=/GLL2024-DCDS.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Gao, Y., J. -G. Liu, O. Tse. <a href="https://doi.org/10.48550/arXiv.2311.07795" target="_blank">Optimal control formulation of transition path problems for Markov Jump Processes</a>. submitted.
4. Gao, Y., W. Li, J. -G. Liu. <a href="https://arxiv.org/abs/2408.08505" target="_blank">Fluctuations in Wasserstein dynamics on Graphs</a>. submitted.
5. Gao, Y., N. K. Yip. <a href="https://doi.org/10.48550/arXiv.2312.01584" target="_blank">Homogenization of Wasserstein gradient flows</a>, to appear at European Journal of Applied Mathematics.
6. Gao, Y., D. Qi. <a href="https://doi.org/10.48550/arXiv.2401.10356" target="_blank">Mean Field Games for Controlling Coherent Structures in Nonlinear Fluid Systems</a>. submitted.



### <div id="obstacle">3. Obstacle problem: moving contact lines, lubrication</div>

The dynamics and equilibrium of a droplet on a substrate are important problems with many practical applications such as coating, painting in industries and the adhesion of vesicles in biotechnology. Particularly, the contact line dynamics of a droplet placed on an inclined rough surface are challenging fluid mechanics problems dated back to Young in 1805. The capillary effect, which contributes the leading behaviors of the geometric motion of a small droplet, is characterized by the surface tensions on interfaces separating two different physical phases.

The geometric dynamics of the droplets are described by the mean curvature flow of the capillary surface, coupled with the moving contact lines (where three phases meet), which contributes the leading driven force for the droplet dynamics. The dynamic contact angles tend to go to the equilibrium contact angle (Young's angle) following the contact line speed mechanism proposed by de Gennes. We focus on the 2nd order unconditionally stable numerical schemes for simulating droplets dynamics on a inclined rough surface with topological changes, such that merging and splitting.

After lubrication approximation, we also investigated the resulting fluid thin film system. A spatial variation in a thin lipid layer leads to locally elevated evaporation rates of the tear film, which in turn affects the local salt concentration in the liquid film. After considering all the contributions from evaporation, capillarity and osmolarity, a general model can capture the key features of tear-film dynamics and rupture with power-law mobility functions.


<table border="0" width="900px" style="margin-top:30px;margin-bottom:0px;"/>
    <center>
        <img src="obstacle1.jpg" style="width:500px;"/>
    </center>
    <center style="zoom:100%;">
        Rupture in tear film dynamics with evaporation, capillarity and osmolarity
    </center>
</table>

<table border="0" width="900px" bgcolor="white" style="margin-top:-10px;margin-bottom:30px;"/>
    <tr>
        <td rowspan="3" style="border:1px solid #ffffff;">
            <center>
                <img src="droplet2-small.jpg" style="width:430px;  margin-left:80px;"/>
            </center>
            <center style="zoom:100%; margin-left:40px;">
                Kelvin pendant droplets with bulge or lightbulb shape
            </center>
        </td>
        <td style="border:1px solid #ffffff;">
            <center>
                <img src="droplet1-small.jpg" style="width:430px; margin-right:80px; margin-top:40px;"/ >
            </center>
            <center style="zoom:100%;margin-right:20px;">
                Splitting of droplet due to rough substrate
            </center>           
        </td>
    </tr>
    <tr>
        <td valign="bottom" bgcolor="white" style="border:1px solid #ffffff;">
            <center>
                <img src="droplet3-small.jpg" style="width:430px; margin-right:80px; margin-bottom:30px;"/ >
            </center>
            <center style="zoom:100%; margin-right:20px; margin-bottom:10px;">
                Merging of droplets and contact angle hysteresis
            </center>           
        </td>
    </tr>
</table>

**Related publications:**
1. Gao, Y., H. Ji, J.-G. Liu, and T. P. Witelski. <a href="https://doi.org/10.1016/j.physd.2017.03.005" target="_blank">Global existence of solutions to a tear film model with locally elevated evaporation rates.</a>  Physica D: Nonlinear Phenomena. 350: 13–25. (2017).  *Full text:* <a href=/GJLW2017.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao, Y., and J.-G. Liu. <a href="https://doi.org/10.4171/ifb/451" target="_blank">Gradient flow formulation and second order numerical method for motion by mean curvature and contact line dynamics on rough surface.</a>  Interfaces and Free Boundaries. 23(1): 103–158. (2021)  *Full text:* <a href=/GL2021.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Gao, Y., and J.-G. Liu. <a href="https://doi.org/10.1016/j.physd.2021.133067" target="_blank">Surfactant-dependent contact line dynamics and droplet adhesion on textured substrates: derivations and computations,</a> Physica D: Nonlinear Phenomena. 428: 133067. (2021). *Full text:* <a href=/GL202110.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
4. Gao, Y., and J.-G. Liu. <a href="https://epubs.siam.org/doi/10.1137/20M1338563" target="_blank">Projection method for droplet dynamics on groove-textured surface with merging and splitting,</a> SIAM Journal on Scientific Computing. 44(2): B310–B338. (2022).  *Full text:* <a href=/GL2022.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>


---

### <div id="dislocations">4. Motion of materials defects: dislocations and grain boundaries </div>

Dislocations are line defects in crystalline materials and they play essential roles in understanding materials properties like plastic deformation and in the development of novel materials with robust performance.

The detailed structure in a dislocation core can be described by the Peierls-Nabarro (PN) model, which is a multiscale continuum model that incorporates the atomistic effect by introducing a nonlinear potential describing the nonlinear atomistic interaction across the slip plane of the dislocation. We focus on existence, De Giorgi-type 1D symmetry, uniqueness and asymptotic stability of the original 3D vectorial dislocation model.

**Related publications:**

1. Gao, Y., J.-G. Liu, T. Luo, and Y. Xiang. <a href="http://dx.doi.org/10.3934/dcdsb.2020224" target="_blank">Revisit of the Peierls-Nabarro model for edge dislocations in Hilbert space. </a> Discrete and Continuous Dynamical Systems Series B. 26(6): 3177-3207. (2020)
2. Gao, Y., and J.-G. Liu. <a href="https://doi.org/10.4310/maa.2020.v27.n2.a4" target="_blank">Long time behavior of dynamic solution to Peierls–Nabarro dislocation model.</a>  Methods and Applications of Analysis. 27(2): 161–198. (2020)  *Full text:* <a href=/GL2020_LongTime.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Dong, H., and Y. Gao. <a href="https://doi.org/10.1007/s00526-021-01939-1" target="_blank">Existence and uniqueness of bounded stable solutions to the Peierls–Nabarro model for curved dislocations.</a> Calculus of Variations and Partial Differential Equations. 60(2): 62. (2021).  *Full text:* <a href=/DG2021.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
4. Gao, Y., J.-G. Liu, and Z. Liu. <a href="https://iopscience.iop.org/article/10.1088/1361-6544/ac24e3" target="_blank">Existence and rigidity of the Peierls-Nabarro model for dislocations in high dimensions,</a>  Nonlinearity. 34(11): 7778–7828. (2021). *Full text:* <a href=/GLL2021.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
5. Gao, Y. and J.-M. Roquejoffre. <a href="https://doi.org/10.1137/22M1469791" target="_blank">Asymptotic stability for diffusion with dynamic boundary reaction from Ginzburg-Landau energy</a>. SIAM Mathematical Analysis. 55(2): 1246-1263. (2023)  *Full text:* <a href=/GR2023.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
6. Gao, Y., and J.-M. Scott. <a href="https://doi.org/10.1088/1361-6544/ad1763" target="_blank">Existence and uniqueness of solutions to the Peierls-Nabarro model in anisotropic media</a>. Nonlinearity, 37: 1-30. (2024).  *Full text:* <a href=/Gao_Scott_2024_Nonlinearity.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

---

### <div id="langevin">5. Langevin dynamics, rare events</div>

Langevin dynamics with an energy landscape representing the stable or metastable states are often used to describe various physical system satisfying the fluctuation-dissipation relation. More importantly, irreversible drift-diffusion processes are very common in biochemical reactions and the irreversibility in circulation balance is indeed an primary characteristic of life activities. They have a non-equilibrium stationary state (invariant measure) which does not satisfy detailed balance.

To simulate those Markov processes, designing structure-preserving numerical schemes which enjoys stochastic Q-matrix structure and symmetric decomposition are very important. Those algorithms assign the transition probability on point clouds and thus naturally give random walk approximations for a generic Markov process on a manifold. Thus combining with collected point clouds probing the manifold (induced from nonlinear dimension reduction such as diffusion map), those algorithms can be easily adapted to manifold-related computations such as finding the transition path in a rare event such as protein folding.

Various promising interdisciplinary applications are conducted including efficient sampling enhanced by a mixture flow, auto-inbetweening image transformation, optimal controlled Monte Carlo simulation for conformational transitions and simulations of shape dynamics on manifold.

<table border="0" width="900px" style="margin-top:30px;margin-bottom:10px;"/>
    <tr>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="langevin1-small.jpg" style="margin-right:0px; margin-left:80px; width:430px;"/>
            </center>
            <center style="zoom:100%; margin-left:80px;">
                Aging process of human faces
            </center>
        </td>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="langevin2-small.jpg" style="margin-right:80px; margin-left:0px; width:430px;"/>
            </center>
            <center style="zoom:100%; margin-right:80px;">
                Continental drift process via data-driven simulation
            </center>           
        </td>
    </tr>
    <tr>
        <td valign="center" bgcolor="white" style="border:1px solid #ffffff;">
            <center>
                <img src="langevin3-small.jpg" style="margin-right:0px; margin-left:80px; width:430px;"/>
            </center>
            <center style="zoom:100%; margin-left:80px;">
                Simulated pneumonia invading lungs caused by COVID-19 on CT images
            </center>           
        </td>
        <td valign="center" bgcolor="white" style="border:1px solid #ffffff;">
            <center>
                <img src="langevin4-small.jpg" style="margin-right:0px; margin-right:80px; width:430px; height:150px;"/>
            </center>
            <center style="zoom:100%; margin-right:80px;">
                Transition path simulation via optimally controlled random walk on point clouds
            </center>           
        </td>
    </tr>
</table>

<table border="0" width="900px" style="margin-top:10px;margin-bottom:30px;"/>
    <tr>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="sam_time.jpg" style="margin-right:0px; margin-left:20px; margin-bottom:0px; width:430px;"/>
            </center>
            <center style="zoom:100%; margin-left:20px;margin-bottom:5px;">
                Accelerated sampling triple-banana via irreversible dynamics
            </center>
        </td>
        <td valign="center" style="border:1px solid #ffffff;">
            <center>
                <img src="VG_time_blue.jpg" style="margin-right:20px; margin-left:0px;margin-bottom:20px; width:430px;"/>
            </center>
            <center style="zoom:100%; margin-right:20px;">
                Image transformation immersed in an incompressible mixture flow
            </center>           
        </td>
    </tr>
</table>

**Related publications:**
1. Gao, Y., G. Jin, and J.-G. Liu. <a href="http://dx.doi.org/10.3934/ipi.2021016" target="_blank">Inbetweening auto-animation via Fokker-Planck dynamics and thresholding.</a>  Inverse Problems and Imaging. 15(5): 843-864. (2021) *Full text:* <a href=/GJL2021.pdf target="_blank"><i class="fas fa-file-pdf"></i></a> *Video for facial aging process:* <a href="https://youtu.be/0ylxAXZAeig" target="_blank"> <i class="fab fa-youtube"></i></a>
2. Gao, Y., T. Li, X. Li, and J.-G. Liu. <a href="https://epubs.siam.org/doi/10.1137/21M1437883" target="_blank">Transition path theory for Langevin dynamics on manifold: optimal control and data-driven solver.</a> Multiscale Modeling and Simulation. 21(1):1-33. (2023)  *Full text:* <a href=/GLLL2023.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Gao, Y., J. -G. Liu, and N. Wu. <a href="https://doi.org/10.1016/j.acha.2022.09.003" target="_blank">Data-driven Efficient Solvers for Langevin Dynamics on Manifold in High Dimensions.</a> Applied and Computational Harmonic Analysis. 62(2023):261-309. (2023)  *Full text:* <a href=/GLW2022.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
4. Gao, Y., and J.-G. Liu. <a href="https://arxiv.org/abs/2106.01344" target="_blank">Random walk approximation for irreversible drift-diffusion process on manifold: ergodicity, unconditional stability and convergence</a>. Communications in Computational Physics. 34(1): 132-172. (2023). *Full text:* <a href=/Gao_Liu_CICP23.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
5. Liu, C., Y. Gao, and X. X. Zhang. <a href="https://doi.org/10.1007/s10915-023-02378-0" target="_blank">Structure preserving schemes for Fokker-Planck equations of irreversible processes</a>. Journal of Scientific Computing, 98(4). (2024).  *Full text:* <a href=/LGZ2024-JSC.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

---

### <div id="crystal"> 6. Crystal growth</div>

Epitaxial growth is a process in which adatoms are deposited on a substrate and grow a solid thin film on the substrate. In general, PDEs modeling macroscopic dynamics in non-equilibrium dynamics are usually guided by the underlying competing mechanism at the microscopic level. Meanwhile, an effective description of the microscopic dynamics, using equilibrium Gibbs measure or non-equilibrium optimal twist measure, is suggested by macroscopic observations. We also derive the continuum limit PDE from the surface hopping process on lattice and give validations via kinetic Monte Carlo.

From a larger mesoscopic scale, Epitaxial growth is described by step flow dynamics driven by misfit elasticity between thin film and the substrate. The discrete Burton-Cabrera-Frank (BCF) type models have been proposed by Burton, Cabrera, Frank, Duport, Tersoff, et al.. From the macroscopic view, the governing equations for thin film growth processes are all high order degenerate parabolic equations. We focus on the analytic validation of those continuum models by studying the continuum limit from discrete model, global positive solution, strong solutions with latent singularities and long-time behavior of solutions. The facet formation for some nonlocal misfit elasticity with fat tails is still open.

<table border="0" width="900px" style="margin-top:30px;margin-bottom:30px;"/>
    <tr>
        <td style="border:1px solid #ffffff;">
            <center>
                <img src="crystal1.jpg" style="margin-right:0px; margin-left:100px; height:300px; width:300px;"/>
            </center>
            <center style="zoom:100%;">
                Microscopic surface hopping to BCF step flow
            </center>
        </td>
        <td style="border:1px solid #ffffff;">
            <center>
                <img src="crystal2.jpg" style="margin-right:100px; margin-left:0px; height:250px; width:500px;"/>
            </center>
            <center style="zoom:100%;">
                Latent singularity for slope of crystal profile
            </center>           
        </td>
    </tr>
</table>

**Related publications:**

1. Gao, Y., J.-G. Liu, and J. Lu. <a href="https://doi.org/10.1007/s00332-016-9354-1" target="_blank">Continuum Limit of a Mesoscopic Model with Elasticity of Step Motion on Vicinal Surfaces.</a> Journal of Nonlinear Science. 27(3): 873–926. (2017). *Full text:* <a href=/GLL2017.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao, Y., J.-G. Liu, and J. Lu. <a href="https://doi.org/10.1137/16M1094543" target="_blank">Weak solution of a continuum model for vicinal surface in the attachment-detachment-limited regime. </a> Siam Journal on Mathematical Analysis. 49(3): 1705–1731. (2017). *Full text:* <a href=/GLL2017b.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
3. Gao, Y., J.-G. Liu, X. Y. Lu, and X. Xu. <a href="https://doi.org/10.1007/s00526-018-1326-x" target="_blank">Maximal monotone operator theory and its applications to thin film equation in epitaxial growth on vicinal surface.</a> Calculus of Variations and Partial Differential Equations. 57(2): 55. (2018). *Full text:* <a href=/GLLX2018.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
4. Gao, Y., H. Ji, J.-G. Liu, and T. P. Witelski. <a href="https://doi.org/10.3934/dcdsb.2018170" target="_blank">A vicinal surface model for epitaxial growth with logarithmic free energy.</a>  Discrete and Continuous Dynamical Systems  Series B. 23(10): 4433–4453. (2018). *Full text:* <a href=/GJLW2018.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
5. Gao, Y., J.-G. Liu, and X. Y. Lu. <a href="https://doi.org/10.1051/cocv/2018037" target="_blank">Gradient flow approach to an exponential thin film equation: Global existence and latent singularity.</a>  Esaim  Control, Optimisation and Calculus of Variations. 25(49).  (2019).  *Full text:* <a href=/GLL2018.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
6. Gao, Y.. <a href="https://doi.org/10.1016/j.jde.2019.05.011" target="_blank">Global strong solution with BV derivatives to singular solid-on-solid model with exponential nonlinearity.</a>  Journal of Differential Equations. 267(7): 4429–4447. (2019).  *Full text:* <a href=/G2019.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
7. Gao, Y., J.-G. Liu, J. Lu and J. L. Marzuola. <a href="https://doi.org/10.1088/1361-6544/ab853d" target="_blank">Analysis of a continuum theory for broken bond crystal surface models with evaporation and deposition effects.</a> Nonlinearity. 33(8): 3816-3845. (2020).  *Full text:* <a href=/GLLM2020.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
8. Gao, Y., X. Y. Lu, and C. Wang. <a href="https://doi.org/10.1515/acv-2020-0114" target="_blank">Regularity and monotonicity for solutions to a continuum model of epitaxial growth with nonlocal elastic effects.</a>  Advances in Calculus of Variations. 000010151520200114. (2021). *Full text:* <a href=/GLW2021.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
9. Gao, Y., A.E. Katsevich, J.-G. Liu, J. Lu, and J.L. Marzuola. <a href="https://doi.org/10.2140/paa.2021.3.595" target="_blank">Analysis of a fourth order exponential PDE arising from a crystal surface jump process with Metropolis-type transition rates.</a> Pure and Applied Analysis. 3(4): 595-612. (2022).  *Full text:* <a href=/GKLLM2022.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

---

### <div id="controllability"> 7. Controllability, stabilization for dynamic boundary condition</div>

My research interests also extend to noise control in building materials which derives a system of wave equation coupled with some acoustic boundary conditions. Although there has been some research on system with acoustic boundary condition, there is little result dealing with completely nonlinear oscillatory of boundary materials, especially for uniformly stabilization with only boundary damping.

**Related publications:**

1. Gao, Y., J. Liang, and T. J. Xiao. <a href=/GLX2017.pdf target="_blank">Observability inequality and decay rate for wave equations with nonlinear boundary conditions.</a>  Electronic Journal of Differential Equations. 2017(161): 1-12. (2017). *Full text:* <a href=/GLX2017.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao, Y., J. Liang, and T. J. Xiao. <a href="https://doi.org/10.1137/16M107863X" target="_blank">A new method to obtain uniform decay rates for multidimensional wave equations with nonlinear acoustic boundary conditions.</a>  Siam Journal on Control and Optimization. 56(2): 1303–1320. (2018). *Full text:* <a href=/GLX2018.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

---

### <div id="miscellany">8. Miscellany</div>


**Related publications:**

1. Gao, Y., Y. Gao, and J.-G. Liu. <a href="https://doi.org/10.1090/QAM/1573" target="_blank">Large Time Behavior, bi-Hamiltonian Structure, and Kinetic Formulation for a Complex Burgers Equation.</a>  Quarterly of Applied Mathematics. 79(1): 55-102. (2020).  *Full text:* <a href=/GL2020.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
2. Gao. Y., and J.-G. Liu. <a href="https://dx.doi.org/10.4310/AMSA.2020.v5.n2.a3" target="_blank">A note on parametric Bayesian inference via gradient flows.</a>  Annals of Mathematical Sciences and Applications. 5(2): 261–282. (2020)  *Full text:* <a href=/GL2020b.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>



[^_^]:
	Comment out:
	[Diffusion processes and stochastic analysis on manifolds](https://scholars.duke.edu/individual?uri=https%3A%2F%2Fscholars.duke.edu%2Findividual%2Fdukehttps%3A%2F%2Fscholarsd.duke.edu%2Findividual%2Fmsc58J65)

	[Dimension reduction (Statistics)](https://scholars.duke.edu/individual?uri=http%3A%2F%2Fid.loc.gov%2Fauthorities%2Fsubjects%2Fsh2010000188%23concept)

	[General behavior of solutions of PDE (comparison theorems; oscillation, zeros and growth of solutions; mean value theorems)](https://scholars.duke.edu/individual?uri=https%3A%2F%2Fscholars.duke.edu%2Findividual%2Fdukehttps%3A%2F%2Fscholarsd.duke.edu%2Findividual%2Fmsc35B05)

	[PDE in connection with control problems](https://scholars.duke.edu/individual?uri=https%3A%2F%2Fscholars.duke.edu%2Findividual%2Fdukehttps%3A%2F%2Fscholarsd.duke.edu%2Findividual%2Fmsc35B37)

	[Simulation and numerical modeling](https://scholars.duke.edu/individual?uri=https%3A%2F%2Fscholars.duke.edu%2Findividual%2Fdukehttps%3A%2F%2Fscholarsd.duke.edu%2Findividual%2Fmsc81T80)


	## <div id="tear">2. Tear film evolution</div>

	Fluid thin film is offten more complicated than solid thin film. A spatial variation in a thin lipid layer leads to locally elevated evaporation rates of the tear film, which in turn affects the local salt concentration in the liquid film. After considering all the contributions from evaporation, capillarity and osmolarity, a general model to capture and explore the key features of tear-film dynamics and rupture with power-law mobility functions is investigated.

	**Related publications:**

	1. Gao, Y., J. Liang, and T. J. Xiao. <a href=/GLX2017.pdf target="_blank">Observability inequality and decay rate for wave equations with nonlinear boundary conditions.</a>  Electronic Journal of Differential Equations. 2017(161). (Jul 4, 2017). *Full text:* <a href=/GLX2017.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>
	2. Gao, Y., J. Liang, and T. J. Xiao. <a href="https://doi.org/10.1137/16M107863X" target="_blank">A new method to obtain uniform decay rates for multidimensional wave equations with nonlinear acoustic boundary conditions.</a>  Siam Journal on Control and Optimization. 56(2): 1303–1320. (Jan 1, 2018). *Full text:* <a href=/GLX2018.pdf target="_blank"><i class="fas fa-file-pdf"></i></a>

	---

	## <div id="stochastic"> 6. Applied stochastic analysis</div>

	PDEs modeling macroscopic dynamics in equilibrium/non-equilibrium systems are usually guided by the underlying competing mechanism at the microscopic level. Meanwhile, an effective description of the microscopic dynamics, using equilibrium Gibbs measure or non-equilibrium optimal twist measure, is suggested by macroscopic observations.

	We first focused on deriving the continuum limit PDE from the Markov jumping process on lattice. Then for Markov process on point clouds, which suggest an approximated intrinsic manifold (for instance by diffusion map), we simulate the Fokker-Planck equation on the manifold by constructing an approximate Voronoi tessellation. The constructed Markov process (with transition probability assigned on each adjacent data points) and the approximated energy landscape are foundations to simulate inbetweening transformations and manifold-related sampling/transition path problems in biochemical reactions.

	<a href=/DataDrivenStories.pdf target="_blank">How to resolve the underlying dynamic processes via data-driven algorithms?</a>

	<table border="0" width="1200px" style="margin-top:10px;margin-bottom:20px;"/>
    <tr>
        <td><center>
        <img src="blue.png" style="margin-top:10px;margin-bottom:10px; width:900px;"/>
        </center>
        <center style="zoom:120%;">
        Fig.1 Epitaxial growth
        </center></td>
    <tr>
	</table>
