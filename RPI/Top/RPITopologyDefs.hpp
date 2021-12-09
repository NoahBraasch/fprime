#ifndef RPITopologyDefs_HPP
#define RPITopologyDefs_HPP

#include "Fw/Types/MallocAllocator.hpp"
#include "RPI/Top/FppConstantsAc.hpp"

namespace RPI {

  namespace Allocation {

    // Malloc allocator for topology construction
    extern Fw::MallocAllocator mallocator;

  }

  // State for topology construction
  struct TopologyState {
    TopologyState() :
      hostName(""),
      portNumber(0)
    {

    }
    TopologyState(
        const char *hostName,
        U32 portNumber
    ) :
      hostName(hostName),
      portNumber(portNumber)
    {

    }
    const char* hostName;
    U32 portNumber;
  };

  // Health ping entries
  namespace PingEntries {
    namespace rateGroup10HzComp { enum { WARN = 3, FATAL = 5 }; }
    namespace rateGroup1HzComp { enum { WARN = 3, FATAL = 5 }; }
    namespace cmdDisp { enum { WARN = 3, FATAL = 5 }; }
    namespace cmdSeq { enum { WARN = 3, FATAL = 5 }; }
    namespace chanTlm { enum { WARN = 3, FATAL = 5 }; }
    namespace eventLogger { enum { WARN = 3, FATAL = 5 }; }
    namespace prmDb { enum { WARN = 3, FATAL = 5 }; }
    namespace fileDownlink { enum { WARN = 3, FATAL = 5 }; }
    namespace fileUplink { enum { WARN = 3, FATAL = 5 }; }
  }

}

#endif
